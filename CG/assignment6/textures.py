from OpenGL.GL import *
import sys, ctypes, platform
from numpy import *
from pysoil import *

# contributor : Meghana Sathish

class textures (object):

    # Add any global definitions and/or variables you need here.

    ##
    # This function loads texture data for the GPU.
    #
    # You will need to write this function, and maintain all of the values
    # needed to be sent to the various shaders.
    ##
    def loadTexture( self ) :
        tex_2d = SOIL_load_OGL_texture("smiley.png", SOIL_LOAD_AUTO, SOIL_CREATE_NEW_ID,
                                       SOIL_FLAG_INVERT_Y)
        if( 0 == tex_2d ):
            print( "SOIL loading error: '%s'\n", SOIL_last_result())
        else:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D,tex_2d)


    ###
    # This function sets up the parameters for texture use.
    #
    # You will need to write this function, and maintain all of the values
    # needed to be sent to the various shaders.
    #
    # @param program - The ID of an OpenGL (GLSL) shader program to which
    #  parameter values are to be sent
    ###
    def setUpTexture( self, program ) :
        ambienceCE = 0.5
        diffuseCE = 0.7
        specularityExponent = 10.0
        specularCE = 1.0
        colorLightSource = [1.0, 1.0, 0.0, 1.0]
        positionOfSourceLight = [0.0, 5.0, 2.0, 1.0]
        ambientLightColor = [0.5, 0.5, 0.5, 1.0]

        glUniform4fv(glGetUniformLocation(program, "colorLightSource"), 1, colorLightSource, 0)
        glUniform4fv(glGetUniformLocation(program, "positionOfSourceLight"), 1, positionOfSourceLight, 0)
        glUniform1f(glGetUniformLocation(program, "ambienceCE"), ambienceCE)
        glUniform1f(glGetUniformLocation(program, "diffuseCE"), diffuseCE)
        glUniform1f(glGetUniformLocation(program, "specularCE"), specularCE)
        glUniform1f(glGetUniformLocation(program, "specularityExponent"), specularityExponent)
        glUniform4fv(glGetUniformLocation(program, "ambientLightColor"), 1, ambientLightColor, 0)


