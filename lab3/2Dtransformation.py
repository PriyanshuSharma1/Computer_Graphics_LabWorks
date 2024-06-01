import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import numpy as np
import math

# Function to draw the shape
def draw_shape(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

# Function for 2D translation
def translate(vertices, tx, ty):
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, translation_matrix.T)[:, :2]

# Function for 2D rotation
def rotate(vertices, angle):
    rad = math.radians(angle)
    rotation_matrix = np.array([
        [math.cos(rad), -math.sin(rad), 0],
        [math.sin(rad), math.cos(rad), 0],
        [0, 0, 1]
    ])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, rotation_matrix.T)[:, :2]

# Function for 2D scaling
def scale(vertices, sx, sy):
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, scaling_matrix.T)[:, :2]

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "2D Transformations", None, None)
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

        # Draw the original shape
        glColor3f(1, 0, 0)
        draw_shape(vertices)

        # Apply translation and draw the translated shape
        translated_vertices = translate(vertices, *translation_params)
        translated_vertices = translate(translated_vertices, 200, 0)  # Move to the right
        glColor3f(0, 1, 0)
        draw_shape(translated_vertices)

        # Apply rotation and draw the rotated shape
        rotated_vertices = rotate(vertices, rotation_angle)
        rotated_vertices = translate(rotated_vertices, 0, 200)  # Move up
        glColor3f(0, 0, 1)
        draw_shape(rotated_vertices)

        # Apply scaling and draw the scaled shape
        scaled_vertices = scale(vertices, *scaling_factors)
        scaled_vertices = translate(scaled_vertices, -200, 0)  # Move to the left
        glColor3f(1, 1, 0)
        draw_shape(scaled_vertices)

        # Apply composite transformation (translate -> rotate -> scale)
        composite_vertices = translate(vertices, *translation_params)
        composite_vertices = rotate(composite_vertices, rotation_angle)
        composite_vertices = scale(composite_vertices, *scaling_factors)
        composite_vertices = translate(composite_vertices, 0, -200)  # Move down
        glColor3f(1, 0, 1)
        draw_shape(composite_vertices)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
