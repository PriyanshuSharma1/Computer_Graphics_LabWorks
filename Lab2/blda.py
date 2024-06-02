import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Bresenham's Line Drawing Algorithm for |m| < 1
def draw_line_low(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2 * dy - dx
    y = y1

    glBegin(GL_POINTS)
    for x in range(x1, x2 + 1):
        glVertex2i(x, y)
        if D > 0:
            y += yi
            D -= 2 * dx
        D += 2 * dy
    glEnd()

# Bresenham's Line Drawing Algorithm for |m| >= 1
def draw_line_high(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2 * dx - dy
    x = x1

    glBegin(GL_POINTS)
    for y in range(y1, y2 + 1):
        glVertex2i(x, y)
        if D > 0:
            x += xi
            D -= 2 * dy
        D += 2 * dx
    glEnd()

# Bresenham's Line Drawing Algorithm
def draw_line(x1, y1, x2, y2):
    if abs(y2 - y1) < abs(x2 - x1):
        if x1 > x2:
            draw_line_low(x2, y2, x1, y1)
        else:
            draw_line_low(x1, y1, x2, y2)
    else:
        if y1 > y2:
            draw_line_high(x2, y2, x1, y1)
        else:
            draw_line_high(x1, y1, x2, y2)

# OpenGL initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-400, 400, -400, 400)

# OpenGL rendering
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    draw_line(100, -100, -100, 100)

    glFlush()

# Main function
def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "Bresenham's Line Drawing Algorithm", None, None)
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
