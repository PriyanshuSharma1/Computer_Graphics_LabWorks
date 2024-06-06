import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import numpy as np
import math

# Function to draw the shape (a polygon)
def draw_shape(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

# Function for composite transformation
def composite_transform(vertices, tx, ty, angle, sx, sy):
    rad = math.radians(angle)
    transformation_matrix = np.array([
        [sx * math.cos(rad), -sy * math.sin(rad), tx],
        [sx * math.sin(rad), sy * math.cos(rad), ty],
        [0, 0, 1]
    ])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, transformation_matrix.T)[:, :2]

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "Composite Transformation", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set up the coordinate system
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -400, 400)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Define the initial vertices of the shape (a square)
    vertices = np.array([
        [-50, -50],
        [50, -50],
        [50, 50],
        [-50, 50]
    ])

    # Transformation parameters
    translation_params = (100, 100)
    rotation_angle = 45
    scaling_factors = (2, 0.5)

    while not glfw.window_should_close(window):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Apply composite transformation and draw the resulting shape
        transformed_vertices = composite_transform(vertices, *translation_params, rotation_angle, *scaling_factors)
        glColor3f(1, 0, 1)  # Magenta color
        draw_shape(transformed_vertices)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
