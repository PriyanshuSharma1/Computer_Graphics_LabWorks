import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pi, cos, sin

# Pygame setup
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# OpenGL setup
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

def draw_circle(color, radius):
    glColor3fv(color)
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i*2*pi/100)
        sine = radius * sin(i*2*pi/100)
        glVertex2f(cosine, sine)
    glEnd()

def draw_rectangle(color, width, height):
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(-width/2, -height/2)
    glVertex2f(width/2, -height/2)
    glVertex2f(width/2, height/2)
    glVertex2f(-width/2, height/2)
    glEnd()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Draw a red circle
        draw_circle((1, 0, 0), 1)

        # Draw a blue rectangle
        draw_rectangle((0, 0, 1), 1, 2)

        pygame.display.flip()

if __name__ == "__main__":
    main()