from OpenGL.GL import *
from numpy import *


# contributor: Meghana Sathish (mxs7620@rit.edu)

class lightrocket(object):

    #
    # This function sets up the lighting, material, and shading parameters
    # for the Phong shader for rocket object.
    #
    # You will need to write this function, and maintain all of the values
    # needed to be sent to the vertex shader.
    #
    # @param program - The ID of an OpenGL (GLSL) shader program to which
    #    parameter values are to be sent
    #
    def setUpPhong(self, program) :
        colorAmbience = [0.3, 1.0, 0.25, 1.0]
        #ambient coefficient
        ambienceCE = 0.3
        colorDiffusion = [0.89, 0.1, 0.58, 0.0]
        #diffuse coefficient
        diffuseCE = 0.5
        colorSpecularity = [0.3, 0.7, 0.8, 1.0]
        specularityExponent = 5.0
        #specular coefficient
        specularCE = 0.75
        # Properties of the light source
        colorLightSource = [1.0, 1.0, 1.0, 1.0]
        positionOfSourceLight = [0.0, 5.0, 2.0, 1.0]
        # Properties of the ambient light
        ambientLightColor = [0.25, 0.75, 1.0, 1.0]

        glUniform4fv(glGetUniformLocation(program, "colorLightSource"), 1, colorLightSource, 0)
        glUniform4fv(glGetUniformLocation(program, "positionOfSourceLight"), 1, positionOfSourceLight, 0)
        glUniform4fv(glGetUniformLocation(program, "colorAmbience"), 1, colorAmbience, 0)
        glUniform4fv(glGetUniformLocation(program, "colorDiffusion"), 1, colorDiffusion, 0)
        glUniform4fv(glGetUniformLocation(program, "colorSpecularity"), 1, colorSpecularity, 0)

        glUniform1f(glGetUniformLocation(program, "ambienceCE"), ambienceCE)
        glUniform1f(glGetUniformLocation(program, "diffuseCE"), diffuseCE)
        glUniform1f(glGetUniformLocation(program, "specularCE"), specularCE)
        glUniform1f(glGetUniformLocation(program, "specularityExponent"), specularityExponent)
        glUniform4fv(glGetUniformLocation(program, "ambientLightColor"), 1, ambientLightColor, 0)

