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
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "3D Translation", None, None)
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

    # Translation vector
    translation = np.array([2.0, 1.0, -5.0])

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Set the camera position
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        # Draw the original cube
        glColor3f(1, 0, 0)  # Red color for the original cube
        draw_cube()

        # Apply translation and draw the translated cube
        glPushMatrix()
        glTranslatef(*translation)
        glColor3f(0, 1, 0)  # Green color for the translated cube
        draw_cube()
        glPopMatrix()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
