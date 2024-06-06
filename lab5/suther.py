import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the clipping window
xmin, ymin, xmax, ymax = -0.5, -0.5, 0.5, 0.5

# Function to clip the polygon using Sutherland-Hodgman algorithm
def sutherland_hodgman(subject_polygon, clip_edge):
    def inside(p):
        if clip_edge[2] == 'left':
            return p[0] >= clip_edge[0]
        elif clip_edge[2] == 'right':
            return p[0] <= clip_edge[0]
        elif clip_edge[2] == 'bottom':
            return p[1] >= clip_edge[1]
        elif clip_edge[2] == 'top':
            return p[1] <= clip_edge[1]

    def intersection(p1, p2):
        if clip_edge[2] in ['left', 'right']:
            x = clip_edge[0]
            y = p1[1] + (clip_edge[0] - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0])
        else:
            y = clip_edge[1]
            x = p1[0] + (clip_edge[1] - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
        return [x, y]

    output_list = subject_polygon
    for edge in clip_edge:
        input_list = output_list
        output_list = []
        if len(input_list) == 0:
            break
        s = input_list[-1]
        for p in input_list:
            if inside(p):
                if not inside(s):
                    output_list.append(intersection(s, p))
                output_list.append(p)
            elif inside(s):
                output_list.append(intersection(s, p))
            s = p

    return output_list

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

    # Original polygon
    subject_polygon = [[-0.7, -0.7], [0.7, -0.7], [0.7, 0.7], [-0.7, 0.7]]
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    for vertex in subject_polygon:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    # Clipped polygon
    clip_edges = [
        [xmin, ymin, 'left'],
        [xmax, ymin, 'right'],
        [xmin, ymin, 'bottom'],
        [xmin, ymax, 'top']
    ]
    clipped_polygon = subject_polygon
    for edge in clip_edges:
        clipped_polygon = sutherland_hodgman(clipped_polygon, edge)

    if clipped_polygon:
        glColor3f(0, 1, 0)
        glBegin(GL_POLYGON)
        for vertex in clipped_polygon:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

    glFlush()

# Main function
def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "Sutherland-Hodgman Polygon Clipping", None, None)
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
