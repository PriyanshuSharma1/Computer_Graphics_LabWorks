import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 10
PADDLE_SPEED = 10
BALL_SPEED = 5
FONT_SIZE = 32  # Font size for game over message
RETRY_BUTTON_WIDTH = 200
RETRY_BUTTON_HEIGHT = 50

# Initialize Pygame
pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)

# Set up OpenGL
gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
glClearColor(0, 0, 0, 1)

# Define paddle class
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

# Define ball class
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

# Create paddles and ball objects
def reset_game():
    global left_paddle, right_paddle, ball, game_over
    left_paddle = Paddle(20, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(
        WINDOW_WIDTH - 20 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    )
    ball = Ball(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2)
    game_over = False


reset_game()

# Font and button setup
game_over_font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
button_font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, (0,0,0), color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos2f(x, y)
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

    text_x = x + (width - button_font.size(text)[0]) // 2
    text_y = y + (height - button_font.size(text)[1]) // 2
    draw_text(text, button_font, (255, 0, 0), text_x, text_y)

def game_over_screen():
    global retry_button_pressed
    glClearColor(0.2, 0.2, 0.2, 1.0)  # Dark gray background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw "GAME OVER" text
    game_over_text = "GAME OVER"
    text_width, text_height = game_over_font.size(game_over_text)
    text_x = (WINDOW_WIDTH - text_width) // 2
    text_y = (WINDOW_HEIGHT - text_height) // 2 + 50
    draw_text("GAME OVER", game_over_font, (255, 0, 0), 300, 300)

    # Draw retry button
    button_x = (WINDOW_WIDTH - RETRY_BUTTON_WIDTH) // 2
    button_y = text_y - 100
    draw_button(button_x, button_y, RETRY_BUTTON_WIDTH, RETRY_BUTTON_HEIGHT, "Retry")

    pygame.display.flip()

    # Handle events
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


# Main game loop
left_player_score = 0 
right_player_score = 0 
retry_button_pressed =False
while True:
    score_diff = abs(left_player_score-right_player_score)
    if score_diff >= 2 or game_over:
        game_over = True
        game_over_screen()
        if retry_button_pressed:
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
            reset_game()
        elif ball.x > WINDOW_WIDTH:
            # Right player missed, update score
            left_player_score += 1
            reset_game()

        left_paddle.draw()
        right_paddle.draw()
        ball.draw()

        left_score_x = 20  # Left margin
        left_score_y = WINDOW_HEIGHT - FONT_SIZE - 10  # Bottom of the screen

        right_score_x = WINDOW_WIDTH - 50 
        right_score_y = left_score_y  # Same y-position as left score

        # Draw left and right player scores
        draw_text(str(left_player_score), game_over_font, (255, 0, 255), left_score_x, left_score_y)
        draw_text(str(right_player_score), game_over_font, (255, 0, 255), right_score_x, right_score_y)

        pygame.display.flip()

        pygame.time.wait(10)