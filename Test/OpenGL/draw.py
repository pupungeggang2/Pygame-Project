from OpenGL.GL import *
from OpenGL.GLU import *
import numpy
import var

def draw_cuboid(vertice):
    face = [[0, 2, 1], [0, 3, 2], [0, 7, 3], [0, 4, 7], [3, 6, 2], [3, 7, 6], [4, 5, 6], [4, 6, 7], [1, 2, 6], [1, 6, 5], [0, 1, 5], [0, 5, 4]]
    edge = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4], [1, 5], [2, 6], [3, 7], [4, 5], [5, 6], [6, 7], [7, 4]]

    for i in range(12):
        glUniform3f(var.color, 0.0, 1.0, 0.0)
        temp_array = [vertice[face[i][0]][0], vertice[face[i][0]][1], vertice[face[i][0]][2], vertice[face[i][1]][0], vertice[face[i][1]][1], vertice[face[i][1]][2], vertice[face[i][2]][0], vertice[face[i][2]][1], vertice[face[i][2]][2]]
        glBufferData(GL_ARRAY_BUFFER, 36, numpy.array(temp_array, dtype = numpy.float32), GL_STATIC_DRAW)
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, None)

    for i in range(12):
        glUniform3f(var.color, 0.0, 1.0, 1.0)
        temp_array = [vertice[edge[i][0]][0], vertice[edge[i][0]][1], vertice[edge[i][0]][2], vertice[edge[i][1]][0], vertice[edge[i][1]][1], vertice[edge[i][1]][2]]
        glBufferData(GL_ARRAY_BUFFER, 24, numpy.array(temp_array, dtype = numpy.float32), GL_STATIC_DRAW)
        glDrawElements(GL_LINES, 2, GL_UNSIGNED_INT, None)