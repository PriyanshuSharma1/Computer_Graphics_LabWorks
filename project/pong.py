import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 10
PADDLE_SPEED = 10
BALL_SPEED = 5
FONT_SIZE = 32
RETRY_BUTTON_WIDTH = 200
RETRY_BUTTON_HEIGHT = 50
FPS = 60

# Initialize Pygame
pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Pong Game")

# Set up OpenGL
gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
glClearColor(0.1, 0.1, 0.1, 1)

# Define Paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + PADDLE_WIDTH, self.y)
        glVertex2f(self.x + PADDLE_WIDTH, self.y + PADDLE_HEIGHT)
        glVertex2f(self.x, self.y + PADDLE_HEIGHT)
        glEnd()

    def move_up(self):
        if self.y < WINDOW_HEIGHT - PADDLE_HEIGHT:
            self.y += PADDLE_SPEED

    def move_down(self):
        if self.y > 0:
            self.y -= PADDLE_SPEED

# Define Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def draw(self):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + BALL_SIZE, self.y)
        glVertex2f(self.x + BALL_SIZE, self.y + BALL_SIZE)
        glVertex2f(self.x, self.y + BALL_SIZE)
        glEnd()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y <= 0 or self.y + BALL_SIZE >= WINDOW_HEIGHT:
            self.dy *= -1

        # Handle paddle collision
        if (
            self.x <= left_paddle.x + PADDLE_WIDTH
            and self.y + BALL_SIZE >= left_paddle.y
            and self.y <= left_paddle.y + PADDLE_HEIGHT
        ):
            self.dx *= -1

        if (
            self.x + BALL_SIZE >= right_paddle.x
            and self.y + BALL_SIZE >= right_paddle.y
            and self.y <= right_paddle.y + PADDLE_HEIGHT
        ):
            self.dx *= -1

# Game setup
def reset_game():
    global left_paddle, right_paddle, ball, game_over, left_player_score, right_player_score
    left_paddle = Paddle(20, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(
        WINDOW_WIDTH - 20 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    )
    ball = Ball(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2)
    game_over = False
    left_player_score = 0
    right_player_score = 0

reset_game()

# Font setup
pygame.font.init()
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glWindowPos2f(x, y)
    glDrawPixels(
        text_surface.get_width(),
        text_surface.get_height(),
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        text_data,
    )

def draw_button(x, y, width, height, text):
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    text_x = x + (width - font.size(text)[0]) // 2
    text_y = y + (height - font.size(text)[1]) // 2
    draw_text(text, font, (255, 0, 0), text_x, text_y)

def game_over_screen():
    global retry_button_pressed
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    game_over_text = "GAME OVER"
    text_width, text_height = font.size(game_over_text)
    text_x = (WINDOW_WIDTH - text_width) // 2
    text_y = (WINDOW_HEIGHT - text_height) // 2 + 50
    draw_text(game_over_text, font, (255, 255, 255), text_x, text_y)

    button_x = (WINDOW_WIDTH - RETRY_BUTTON_WIDTH) // 2
    button_y = text_y - 100
    draw_button(button_x, button_y, RETRY_BUTTON_WIDTH, RETRY_BUTTON_HEIGHT, "Retry")

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (button_x <= mouse_x <= button_x + RETRY_BUTTON_WIDTH) and (
                button_y <= mouse_y <= button_y + RETRY_BUTTON_HEIGHT
            ):
                retry_button_pressed = True

def draw_button(x, y, width, height, text):
    glColor3f(0, 0, 0)  # Black background
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    text_x = x + (width - font.size(text)[0]) // 2
    text_y = y + (height - font.size(text)[1]) // 2
    draw_text(text, font, (255, 255, 255), text_x, text_y)

    # Draw rounded corners
    draw_rounded_corners(x, y, width, height, radius=10)

def draw_rounded_corners(x, y, width, height, radius=10):
    num_segments = 30
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        angle = i * 2 * math.pi / num_segments
        glVertex2f(x + width - radius + radius * math.cos(angle), y + height - radius + radius * math.sin(angle))
    glEnd()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos2f(x, y)
    glDrawPixels(
        text_surface.get_width(),
        text_surface.get_height(),
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        text_data,
    )


# Main game loop
retry_button_pressed = False

def main_game_loop():
    global retry_button_pressed, left_player_score, right_player_score, game_over, ball

    clock = pygame.time.Clock()

    while True:
        score_diff = abs(left_player_score - right_player_score)
        if score_diff >= 2 or game_over:
            game_over = True
            game_over_screen()
            if retry_button_pressed:
                retry_button_pressed = False
                reset_game()
        else:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[K_w]:
                left_paddle.move_up()
            if keys[K_s]:
                left_paddle.move_down()
            if keys[K_DOWN]:
                right_paddle.move_down()
            if keys[K_UP]:
                right_paddle.move_up()

            # Update game logic
            ball.move()

            # Check for game over (ball goes out of bounds)
            if ball.x + BALL_SIZE < 0:
                # Left player missed, update score
                right_player_score += 1
                if abs(left_player_score - right_player_score) >= 2:
                    game_over = True
            elif ball.x > WINDOW_WIDTH:
                # Right player missed, update score
                left_player_score += 1
                if abs(left_player_score - right_player_score) >= 2:
                    game_over = True

            left_paddle.draw()
            right_paddle.draw()
            ball.draw()

            left_score_x = 20
            left_score_y = WINDOW_HEIGHT - FONT_SIZE - 10
            right_score_x = WINDOW_WIDTH - 50
            right_score_y = left_score_y

            # Draw left and right player scores
            draw_text(str(left_player_score), font, (255, 255, 255), left_score_x, left_score_y)
            draw_text(str(right_player_score), font, (255, 255, 255), right_score_x, right_score_y)

            pygame.display.flip()

            clock.tick(FPS)

if __name__ == "__main__":
    main_game_loop()
