from OpenGL.GL import *
from numpy import *

# contributor: Meghana Sathish (mxs7620@rit.edu)

class lighting (object):

    #
    # This function sets up the lighting, material, and shading parameters
    # for the Phong shader for pyramid.
    #
    # You will need to write this function, and maintain all of the values
    # needed to be sent to the vertex shader.
    #
    # @param program - The ID of an OpenGL (GLSL) shader program to which
    #    parameter values are to be sent
    #
    def setUpPhong( self,  program ) :
        colorAmbience = [ 0.5, 0.1, 0.9, 1.0 ]
        ambienceCE = 0.5
        colorDiffusion = [ 0.19, 0.3, 0.4, 1.0 ]
        diffuseCE = 0.7
        colorSpecularity = [ 1.0, 1.0, 1.0, 1.0 ]
        specularityExponent = 10.0
        specularCE = 1.0
         # Properties of the light source
        colorLightSource = [ 1.3, 0.5, 1.5, 1.0 ]
        positionOfSourceLight = [ 0.8, 2.5, 0.5, 1.0 ]
         # Properties of the ambient light
        ambientLightColor = [ 0.5, 0.5, 0.5, 1.0 ]

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

        
