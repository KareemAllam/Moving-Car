from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0, 0, 0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10, 10, 10 ,0, 0, 0, 0, 1, 0)
#-------------------------------------------
x=0
Theta=0
def ROAD():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glBegin(GL_POLYGON)
    glColor3d(0, 1, 1)
    glVertex3d(-1+x/2, 0, 3)
    glVertex3d(-1+x/2, 0, -4)
    glVertex3d(x/2, 0, -4)
    glVertex3d(x/2, 0, 3)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3d(1, 1, 1)
    glVertex3d(-30, 0, 20)
    glVertex3d(-60, 0, -5)
    glVertex3d(15, 0, -10)
    glVertex3d(15, 0, 5)
    glEnd()
    glPopAttrib()
    glPopMatrix()

def draw():
#Top
    global x
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    ROAD()
    glColor3f(1, 1, 0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)
#Base
    glColor3f(1,0,0.3)
    glLoadIdentity()
    glTranslate(x,.25*5,0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
#-----------------------------------------------------------
#Tires
    global Theta
    glColor3f(0, 0, 1)                  #
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,2.5*0.5)
    glRotatef(Theta,0,0,1)
    glutSolidTorus(0.125,.5,12,8)        #
    glColor3f(0, 0, 1)                  #
    glLoadIdentity()
    glTranslate(x+2.5, -2.5 * .25, -2.5 * 0.5)
    glRotatef(Theta, 0, 0, 1)
    glutSolidTorus(0.125, .5, 12, 8)     #
    glColor3f(0, 0, 1)                  #
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * .25, -2.5 * 0.5)
    glRotatef(Theta, 0, 0, 1)
    glutSolidTorus(0.125, .5, 12, 8)     #
    glColor3f(0, 0, 1)                  #
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * .25, 2.5 * 0.5)
    glRotatef(Theta, 0, 0, 1)
    glutSolidTorus(0.125, .5, 12, 8)     #
    x += 0.05
    Theta-= 0.11
    glFlush()
#-----------------------------------
x+= 0.05
Theta-= 0.11
#---------------------
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()