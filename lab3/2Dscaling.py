import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import numpy as np

def draw_shape(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def scale(vertices, sx, sy):
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, scaling_matrix.T)[:, :2]

def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 800, "2D Scaling", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -400, 400)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    vertices = np.array([
        [-50, -50],
        [50, -50],
        [50, 50],
        [-50, 50]
    ])

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(1, 0, 0)  # Original shape color
        draw_shape(vertices)

        scaled_vertices = scale(vertices, 2, 0.5)
        glColor3f(0, 1, 0)  # Scaled shape color
        draw_shape(scaled_vertices)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
