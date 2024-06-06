import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Define vertices of a 3D cube
vertices = [
    [1, 1, -1],
    [-1, 1, -1],
    [-1, 1, 1],
    [1, 1, 1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, -1, 1],
    [1, -1, 1]
]

# Define edges of the cube
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Draw a 3D cube
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Translation transformation
def translate(x, y, z):
    glTranslatef(x, y, z)

# Rotation transformation
def rotate(angle, x, y, z):
    glRotatef(angle, x, y, z)

# Scaling transformation
def scale(sx, sy, sz):
    glScalef(sx, sy, sz)

# Shearing transformation
def shear(sxy, sxz, syx, syz, szx, szy):
    shear_matrix = [
        [1, sxy, sxz, 0],
        [syx, 1, syz, 0],
        [szx, szy, 1, 0],
        [0, 0, 0, 1]
    ]
    glMultMatrixf(shear_matrix)

# OpenGL initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, 1, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# OpenGL rendering
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Draw the original cube
    glColor3f(1, 0, 0)
    draw_cube()

    # Apply translation and draw the translated cube
    glPushMatrix()
    translate(2, 0, 0)
    glColor3f(0, 1, 0)
    draw_cube()
    glPopMatrix()

    # Apply rotation and draw the rotated cube
    glPushMatrix()
    rotate(45, 1, 1, 0)
    glColor3f(0, 0, 1)
    draw_cube()
    glPopMatrix()

    # Apply scaling and draw the scaled cube
    glPushMatrix()
    scale(0.5, 1.5, 0.5)
    glColor3f(1, 1, 0)
    draw_cube()
    glPopMatrix()

    # Apply shearing and draw the sheared cube
    glPushMatrix()
    shear(0.5, 0, 0, 0.5, 0, 0)
    glColor3f(1, 0, 1)
    draw_cube()
    glPopMatrix()

    glFlush()

# Main function
def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "3D Transformations", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # OpenGL initialization
    init()

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here
        display()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
