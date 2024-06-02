import glfw
from OpenGL.GL import*
from OpenGL.GLU import*

def draw_line(x1,y1, x2, y2):
    dx= x2-x1
    dy=y2-y1

    steps=max(abs(dx),abs(dy))
    x_inc=dx/steps
    y_inc=dy/steps
    x=x1
    y=y1
    glBegin(GL_POINTS)
    for i in range(steps):
        glVertex2i(round(x),round(y))
        x+=x_inc
        y+=y_inc
    glEnd()

def main():
    if not glfw.init():
        return
    window =glfw.create_window(800,800,"DDA Line Drawing Algorithm",None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glViewport(500,500,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()    
    gluOrtho2D(-400,400,-400,400)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1,0,0)
        glPointSize(3.0)
        draw_line(-100,-100,100,100)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

if __name__=="__main__":
    main()