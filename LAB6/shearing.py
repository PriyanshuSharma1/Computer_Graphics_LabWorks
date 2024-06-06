import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Define vertices for a cube
vertices = [
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
]

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

# Function to draw the cube
def draw_cube(vertices):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def shear_vertices(vertices, shx, shy, shz):
    shearing_matrix = np.array([
        [1, shx, shx, 0],
        [shy, 1, shy, 0],
        [shz, shz, 1, 0],
        [0, 0, 0, 1]
    ])

    sheared_vertices = []
    for vertex in vertices:
        vertex = np.append(vertex, 1)
        sheared_vertex = np.dot(shearing_matrix, vertex)
        sheared_vertices.append(sheared_vertex[:3])

    return sheared_vertices

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "3D Shearing", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)

    # Set the perspective
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Shearing factors
    shx, shy, shz = 0.5, 0.2, 0.0

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Set the camera position
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        # Draw the original cube
        glColor3f(1, 0, 0)  # Red color for the original cube
        draw_cube(vertices)

        # Apply shearing and draw the sheared cube
        sheared_vertices = shear_vertices(vertices, shx, shy, shz)
        glColor3f(0, 1, 0)  # Green color for the sheared cube
        draw_cube(sheared_vertices)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
