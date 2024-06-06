import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the clipping window
xmin, ymin, xmax, ymax = -0.5, -0.5, 0.5, 0.5

# Function to clip the line using Liang-Barsky algorithm
def liang_barsky(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]
    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return None
        if p[i] < 0:
            u1 = max(u1, q[i] / p[i])
        if p[i] > 0:
            u2 = min(u2, q[i] / p[i])
    
    if u1 > u2:
        return None

    x0_clip = x0 + u1 * dx
    y0_clip = y0 + u1 * dy
    x1_clip = x0 + u2 * dx
    y1_clip = y0 + u2 * dy

    return (x0_clip, y0_clip, x1_clip, y1_clip)

# OpenGL initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1, 1, -1, 1)

# OpenGL rendering
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the clipping window
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()

    # Original line
    x0, y0, x1, y1 = -0.7, -0.7, 0.7, 0.7
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()

    # Clipped line
    clipped_line = liang_barsky(x0, y0, x1, y1)
    if clipped_line:
        glColor3f(0, 1, 0)
        glBegin(GL_LINES)
        glVertex2f(clipped_line[0], clipped_line[1])
        glVertex2f(clipped_line[2], clipped_line[3])
        glEnd()

    glFlush()

# Main function
def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "Liang-Barsky Line Clipping", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        display()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
