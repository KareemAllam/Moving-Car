from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 0)
    gluPerspective(100,1,0.1,50)              #Camera Prespective
    gluLookAt(10, 10, 10,0, 0, 0, 0, 1, 0)    #Camera Location
#---------------------------------------------
def chair():
    glPushMatrix()
    gl,90 PushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.6, 0.5, 0)
    glScale(1, 1.2, 0.25)
#BLLeg
    glutSolidCube(4)
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.4, 0.5, 0)
    glScale(0.2, 2, 0.15)
    glTranslate(-35, -6, 7)
#TRLeg
    glutSolidCube(4)
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.4, 0.5, 0)
    glScale(0.2, 2, 0.15)
    glTranslate(-7, -5.5, -26)
#TLLeg
    glutSolidCube(4)
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.4, 0.7, 0)
    glScale(0.1, 1.2, 0.15)
    glTranslate(-12, -3.5, 4)
#Base
    glutSolidCube(4)
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.4, 0.3, 0)
    glScale(1.1,0.25,1)
    glTranslate(-1,-13,1.5)
#BRLeg
    glutSolidCube(4)
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.4, 0.5, 0)
    glScale(0.2, 2, 0.15)
    glTranslate(-7, -5.5, 11)
#BRLeg
    glutSolidCube(4)
    glPopAttrib()
    glPopMatrix()
#---------------------------------
def draw():
    glMatrixMode(GL_MODELVIEW)
    chair()
    glScale(0.6, 1, 1)
    glTranslate(9, 0, 0)
    chair()
    glFlush()
#------------------------------------
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1024, 1024)
glutCreateWindow(b"C H A I R S")
glutDisplayFunc(draw)
myInit()
glutMainLoop()