import pygame
import random
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up the game window
ball_speed=0.1
paddle_speed=0.2
window_width = 800
window_height =700
window = pygame.display.set_mode((window_width, window_height), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Pong Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = paddle_speed

paddle1_x = 20
paddle1_y = window_height // 2 - paddle_height // 2

paddle2_x = window_width - 20 - paddle_width
paddle2_y = window_height // 2 - paddle_height // 2

# Set up the ball
ball_size = 10
ball_speed_x = ball_speed
ball_speed_y = ball_speed
ball_x = window_width // 2 - ball_size // 2
ball_y = window_height // 2 - ball_size // 2

# Set up the score
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Set up the game over screen
game_over = False

# OpenGL setup
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, window_width, window_height, 0)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Function to draw a rectangle
def draw_rect(x, y, width, height, color):
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < window_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < window_height - paddle_height:
        paddle2_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for ball collision with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= paddle2_x - ball_size and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Check for ball collision with walls
    if ball_y <= 0 or ball_y >= window_height - ball_size:
        ball_speed_y = -ball_speed_y

    # Check for ball going out of bounds
    if ball_x <= 0:
        score2 += 1
        ball_x = window_width // 2 - ball_size // 2
        ball_y = window_height // 2 - ball_size // 2
        ball_speed_x = random.choice([-ball_speed, ball_speed])
        ball_speed_y = random.choice([-ball_speed, ball_speed])
    if ball_x >= window_width - ball_size:
        score1 += 1
        ball_x = window_width // 2 - ball_size // 2
        ball_y = window_height // 2 - ball_size // 2
        ball_speed_x = random.choice([-ball_speed,ball_speed])
        ball_speed_y = random.choice([-ball_speed, ball_speed])

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the paddles
    draw_rect(paddle1_x, paddle1_y, paddle_width, paddle_height, WHITE)
    draw_rect(paddle2_x, paddle2_y, paddle_width, paddle_height, WHITE)

    # Draw the ball
    draw_rect(ball_x, ball_y, ball_size, ball_size, WHITE)

    # Draw the score
    score_text = font.render(str(score1) + " - " + str(score2), True, WHITE)
    text_surface = pygame.image.tostring(score_text, 'RGBA', True)
    glRasterPos2d(window_width // 2 - score_text.get_width() // 2, 10)
    glDrawPixels(score_text.get_width(), score_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_surface)

    # Update the display
    pygame.display.flip()

    # Check for game over
    if score1 == 5 or score2 == 5:
        game_over = True

    # Game over screen
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score1 = 0
                    score2 = 0
                    game_over = False
                if event.key == pygame.K_q:
                    running = False
                    game_over = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Display game over text
        game_over_text = font.render("Game Over", True, WHITE)
        text_surface = pygame.image.tostring(game_over_text, 'RGBA', True)
        glRasterPos2d(window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2)
        glDrawPixels(game_over_text.get_width(), game_over_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_surface)

        # Display retry and exit instructions
        retry_text = font.render("Press 'R' to retry", True, WHITE)
        text_surface = pygame.image.tostring(retry_text, 'RGBA', True)
        glRasterPos2d(window_width // 2 - retry_text.get_width() // 2, window_height // 2 + retry_text.get_height() // 2)
        glDrawPixels(retry_text.get_width(), retry_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_surface)

        exit_text = font.render("Press 'Q' to exit", True, WHITE)
        text_surface = pygame.image.tostring(exit_text, 'RGBA', True)
        glRasterPos2d(window_width // 2 - exit_text.get_width() // 2, window_height // 2 + exit_text.get_height() // 2 + retry_text.get_height())
        glDrawPixels(exit_text.get_width(), exit_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_surface)

        # Update the display
        pygame.display.flip()

# Quit the game
pygame.quit()
