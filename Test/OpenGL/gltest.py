import pygame, sys
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL.shaders
import numpy
import draw
import var

class Rot():
    rotation_matrix_x = numpy.array([
        [1, 0, 0, 0],
        [0, numpy.cos(0.01), -numpy.sin(0.01), 0],
        [0, numpy.sin(0.01), numpy.cos(0.01), 0],
        [0, 0, 0, 1]], dtype = numpy.float32)
    
    rotation_matrix_y = numpy.array([
        [numpy.cos(0.02), 0, numpy.sin(0.02), 0],
        [0, 1, 0, 0],
        [-numpy.sin(0.02), 0, numpy.cos(0.02), 0],
        [0, 0, 0, 1]], dtype = numpy.float32)

def main():
    window = pygame.display.set_mode([1280, 800], pygame.OPENGL|pygame.DOUBLEBUF)
    var.clock = pygame.time.Clock()
    indices = [0, 1, 2]
    indices = numpy.array(indices, dtype= numpy.uint32)

    vertex_shader = """
    #version 110
    attribute vec3 position;
    uniform mat4 projection;

    void main()
    {
        gl_Position = projection * vec4(position.x, position.y, position.z, 1.0);
    }
    """

    fragment_shader = """
    #version 110
    uniform vec3 color;

    void main()
    {
        gl_FragColor = vec4(color, 1.0);
    }
    """
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    
    glLinkProgram(shader)
    glUseProgram(shader)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 12, indices, GL_STATIC_DRAW)

    var.position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(var.position, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
    glEnableVertexAttribArray(var.position)

    var.color = glGetUniformLocation(shader, "color")
    var.projection = glGetUniformLocation(shader, "projection")

    glUniformMatrix4fv(var.projection, 1, False, [
        [2/3.2, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0.5, 0],
        [0, 0, 0, 1],
    ])

    glClearColor(0.0, 0.0, 1.0, 1.0)
    glLineWidth(4)
    var.cuboid = numpy.array([[0, 0, 1], [1, 0, 1], [1, 0, 0], [0, 0, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0], [0, 1, 0]], dtype = numpy.float32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        var.clock.tick(var.FPS)
        glClear(GL_COLOR_BUFFER_BIT)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        draw.draw_cuboid(var.cuboid)
        #print(var.cuboid)

        for i in range(len(var.cuboid)):
            temp_vec = numpy.array([var.cuboid[i][0], var.cuboid[i][1], var.cuboid[i][2], 1], dtype = numpy.float32)
            temp_vec = numpy.matmul(Rot.rotation_matrix_x, temp_vec)
            temp_vec = numpy.matmul(Rot.rotation_matrix_y, temp_vec)
            var.cuboid[i][0] = temp_vec[0] / temp_vec[3]
            var.cuboid[i][1] = temp_vec[1] / temp_vec[3]
            var.cuboid[i][2] = temp_vec[2] / temp_vec[3]

        pygame.display.flip()

if __name__ == "__main__":
    main()