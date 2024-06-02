import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define vertices for a cube
vertices = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

# Define edges for a cube
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Define colors for the cube
colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (0, 1, 1)   # Cyan
]

# Define rotation angle
angle = 0

# Function to draw the cube
def draw_cube():
    glLineWidth(2)
    glBegin(GL_LINES)
    for edge_id, (i, j) in enumerate(edges):
        glColor3fv(colors[edge_id % len(colors)])
        glVertex3fv(vertices[i])
        glVertex3fv(vertices[j])
    glEnd()

# Function to handle key events
def key_events():
    global angle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += 1
    if keys[pygame.K_RIGHT]:
        angle -= 1

# Main function
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key_events()

        glRotatef(angle, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()