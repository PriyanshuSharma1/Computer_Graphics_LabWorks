import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D

def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    tworx2 = 2 * rx2
    twory2 = 2 * ry2
    p = round(ry2 - (rx2 * ry) + (0.25 * rx2))

    glBegin(GL_POINTS)
    while tworx2 * y >= twory2 * x:
        glVertex2i(xc + x, yc + y)
        glVertex2i(xc - x, yc + y)
        glVertex2i(xc + x, yc - y)
        glVertex2i(xc - x, yc - y)
        x += 1
        if p < 0:
            p += twory2 * x + ry2
        else:
            y -= 1
            p += twory2 * x - tworx2 * y + ry2

    p = round(ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2)
    while y >= 0:
        glVertex2i(xc + x, yc + y)
        glVertex2i(xc - x, yc + y)
        glVertex2i(xc + x, yc - y)
        glVertex2i(xc - x, yc - y)
        y -= 1
        if p > 0:
            p += rx2 - tworx2 * y
        else:
            x += 1
            p += twory2 * x - tworx2 * y + rx2
    glEnd()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 800, "Mid-point Ellipse Drawing Algorithm", None, None)
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
        glPointSize(1.0)
        glColor3f(0, 1, 0)
        draw_ellipse(0, 0, 150, 100)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
