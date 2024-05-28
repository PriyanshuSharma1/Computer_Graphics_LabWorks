import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import math

# Initialize GLFW
if not glfw.init():
    raise Exception("GLFW can't be initialized")

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(800, 800, "2D Transformations", None, None)
if not window:
    glfw.terminate()
    raise Exception("GLFW window can't be created")

# Make the window's context current
glfw.make_context_current(window)

# Set up the viewport
glViewport(0, 0, 800, 800)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-400, 400, -400, 400, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Define the vertices of the triangle
vertices = np.array([
    [0, 100, 1],
    [-100, -100, 1],
    [100, -100, 1]
], dtype=np.float32)

# Function to draw a triangle
def draw_triangle(verts):
    glBegin(GL_TRIANGLES)
    for vertex in verts:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

# Function to apply a transformation matrix to the vertices
def apply_transformation(verts, matrix):
    return np.dot(verts, matrix.T)

# Function for 2D translation
def translate(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ], dtype=np.float32)

# Function for 2D rotation
def rotate(angle):
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    return np.array([
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0, 0, 1]
    ], dtype=np.float32)

# Function for 2D scaling
def scale(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ], dtype=np.float32)

# Function for 2D reflection
def reflect(axis):
    if axis == 'x':
        return np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ], dtype=np.float32)
    elif axis == 'y':
        return np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype=np.float32)

# Function for 2D shearing
def shear(shx, shy):
    return np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ], dtype=np.float32)

# Function for composite transformation
def composite_transform():
    # Example: Rotate by 45 degrees, then translate by (50, 100), then scale by (2, 0.5)
    return np.dot(np.dot(translate(50, 100), rotate(45)), scale(2, 0.5))

# Main loop
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original triangle
    glColor3f(1, 0, 0)  # Red color
    draw_triangle(vertices)

    # Apply and draw translated triangle
    translated_vertices = apply_transformation(vertices, translate(100, 50))
    glColor3f(0, 1, 0)  # Green color
    draw_triangle(translated_vertices)

    # Apply and draw rotated triangle
    rotated_vertices = apply_transformation(vertices, rotate(45))
    glColor3f(0, 0, 1)  # Blue color
    draw_triangle(rotated_vertices)

    # Apply and draw scaled triangle
    scaled_vertices = apply_transformation(vertices, scale(2, 0.5))
    glColor3f(1, 1, 0)  # Yellow color
    draw_triangle(scaled_vertices)

    # Apply and draw reflected triangle (about x-axis)
    reflected_vertices = apply_transformation(vertices, reflect('x'))
    glColor3f(1, 0, 1)  # Magenta color
    draw_triangle(reflected_vertices)

    # Apply and draw sheared triangle
    sheared_vertices = apply_transformation(vertices, shear(1, 0))
    glColor3f(0, 1, 1)  # Cyan color
    draw_triangle(sheared_vertices)

    # Apply and draw composite transformed triangle
    composite_vertices = apply_transformation(vertices, composite_transform())
    glColor3f(0.5, 0.5, 0.5)  # Gray color
    draw_triangle(composite_vertices)

    glfw.swap_buffers(window)
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()
