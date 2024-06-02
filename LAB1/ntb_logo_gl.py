import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *


def draw_polygon(color, vertices):
    glColor3f(*[c/255.0 for c in color])
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()


def draw_circle(color, center, radius, segments=100):
    glColor3f(*[c/255.0 for c in color])
    glBegin(GL_POLYGON)
    for i in range(segments):
        theta = 2.0 * 3.1415926 * i / segments
        x = radius * cos(theta)
        y = radius * sin(theta)
        glVertex2f(x + center[0], y + center[1])
    glEnd()


def draw_rect(color, rect):
    x, y, width, height = rect
    draw_polygon(color, [(x, y), (x + width, y),
                 (x + width, y + height), (x, y + height)])


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Blue color
    blue = (54, 60, 146)

    # White color
    white = (255, 255, 255)

    # Red color
    red = (221, 0, 39)

    # Draw first mountain
    draw_polygon(blue, [(680, 414), (295, 776), (1067, 776)])

    # Draw second mountain
    draw_polygon(blue, [(928, 564), (563, 834), (1292, 834)])

    # Draw snow on first mountain
    draw_polygon(white, [(680, 432), (590, 522), (770, 522)])

    # Draw front of second mountain
    draw_polygon(white, [(928, 599), (630, 843), (1226, 843)])

    # Draw stupa border
    draw_circle(blue, (418, 1024), 437)

    # Draw face border
    draw_rect(blue, (291, 439, 203, 172))

    # Draw shrine
    draw_polygon(blue, [(393, -17), (296, 441), (489, 441)])

    # Draw stupa front
    draw_circle(white, (419, 1024), 402)

    # Draw face front
    draw_rect(white, (307, 461, 167, 138))

    # Draw head top
    draw_polygon(red, [(393, 370), (337, 441), (449, 441)])

    # Draw head top light
    draw_polygon(white, [(393, 389), (353, 441), (433, 441)])

    # Draw head hat
    draw_rect(red, (281, 439, 223, 27))

    # Draw mask
    draw_rect(white, (0, 539, 433, 485))

    # Draw bottom beam
    draw_rect(red, (22, 783, 472, 31))

    # Draw bottom layer
    draw_polygon(blue, [(252, 609), (27, 776), (477, 776)])

    # Draw gap
    draw_rect(white, (137, 633, 229, 32))

    # Draw top beam
    draw_rect(red, (92, 607, 314, 26))

    # Draw top layer
    draw_polygon(blue, [(247, 461), (98, 598), (395, 598)])

    # Draw gap
    draw_polygon(white, [(247, 461), (190, 511), (303, 511)])

    # Draw gap in shrine
    for i in range(72, 356, 31):
        draw_rect(white, (306, i, 178, 14))

    # Draw shrine
    draw_polygon(blue, [(246, 466), (228, 499), (263, 499)])

    # Draw text rectangles
    draw_rect(white, (19, 874, 45, 150))
    draw_rect(white, (167, 874, 45, 150))
    draw_rect(white, (370, 874, 49, 150))
    draw_rect(white, (300, 874, 189, 37))
    draw_rect(white, (579, 874, 48, 150))
    draw_rect(white, (709, 874, 46, 150))
    draw_rect(white, (579, 930, 176, 37))
    draw_rect(white, (579, 977, 176, 37))
    draw_rect(white, (579, 874, 176, 37))

    # Draw text triangles
    draw_polygon(
        white, [(62.5, 875.5), (170.5, 963.5), (173.5, 1022.5)])
    draw_polygon(
        white, [(62.5, 875.5), (62.5, 940.5), (173.5, 1022.5)])

    pygame.display.flip()


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    global screen
    screen = pygame.display.set_mode(
        (1024, 1024), DOUBLEBUF | OPENGL)  # Set screen size
    pygame.display.set_caption("NTB Logo")    # Set window title

    # Set up OpenGL
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Invert the y-axis to match Pygame's coordinate system
    glOrtho(0, 1024, 1024, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the loop when the user closes the window

        draw()  # Call the draw function to draw the logo with "NTB" integrated

    pygame.quit()  # Clean up and quit Pygame when the loop exits


if __name__ == "__main__":
    main()
