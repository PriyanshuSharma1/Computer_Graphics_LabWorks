import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import numpy as np
import math

def draw_shape(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def rotate(vertices, angle):
    rad = math.radians(angle)
    rotation_matrix = np.array([
        [math.cos(rad), -math.sin(rad), 0],
        [math.sin(rad), math.cos(rad), 0],
        [0, 0, 1]
    ])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, rotation_matrix.T)[:, :2]

def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 800, "2D Rotation", None, None)
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

        rotated_vertices = rotate(vertices, 45)
        glColor3f(0, 1, 0)  # Rotated shape color
        draw_shape(rotated_vertices)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
