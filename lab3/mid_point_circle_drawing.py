import glfw
from OpenGL.GL import *
import math
from OpenGL.GLU import gluOrtho2D

def draw_circle(xc, yc, r):
    x = r
    y = 0
    d = 1 - r

    glBegin(GL_POINTS)
    while y <= x:
        glVertex2i(xc + x, yc + y)
        glVertex2i(xc - x, yc + y)
        glVertex2i(xc + x, yc - y)
        glVertex2i(xc - x, yc - y)
        glVertex2i(xc + y, yc + x)
        glVertex2i(xc - y, yc + x)
        glVertex2i(xc + y, yc - x)
        glVertex2i(xc - y, yc - x)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    glEnd()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 800, "Mid-point Circle Drawing Algorithm", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -400, 400)


    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 0, 0)
        glPointSize(1.0)
        draw_circle(0, 0, 100)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
