import pygame, sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1))

edge = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 7), (7, 5), (5, 6), (6, 4), (3, 6), (0, 4), (2, 5), (1, 7))

def cube():
    glBegin(GL_LINES)
    for e in edge:
        for vertex in e:
            glVertex3iv(vertices[vertex])
    glEnd()

pygame.init()
pygame.display.set_mode([1280, 720], DOUBLEBUF|OPENGL|pygame.SCALED)
pygame.display.set_caption("Sample OpenGL")

gluPerspective(45, (1280 / 720), 0.1, 50.0)
glTranslatef(0, 0, 0-5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    glRotatef(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    cube()
    pygame.display.flip()
    pygame.time.wait(15)
