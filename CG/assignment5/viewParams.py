# program to implement perspective and orthogonal projections of a teapot.
# author: Meghana Sathish (mxs7620@rit.edu)

from OpenGL.GL import *
from numpy import *

class viewParams(object):
    
    '''
     * This function sets up the view and projection parameter for a frustum
     * projection of the scene. See the assignment description for the values
     * for the projection parameters.
     *
     * You will need to write this function, and maintain all of the values
     * needed to be sent to the vertex shader.
     *
     * @param program - The ID of an OpenGL (GLSL) shader program to which
     *    parameter values are to be sent
     *
    '''
    def setUpFrustrum(self, program):
        #get the toggle variable typeOfProjection from shader.vert and set to
		#a value of 1 to have the Frustum projection.
        loc = glGetUniformLocation(program, "typeOfProjection")
        glUniform1i(loc, 1)

        '''
     * This function sets up the view and projection parameter for an
     * orthographic projection of the scene. See the assignment description
     * for the values for the projection parameters.
     *
     * You will need to write this function, and maintain all of the values
     * needed to be sent to the vertex shader.
     *
     * @param program - The ID of an OpenGL (GLSL) shader program to which
     *    parameter values are to be sent
     *
    '''
    def setUpOrtho(self, program):
        #get the toggle variable typeOfProjection from shader.vert and set to
		#a value of 2 to have the Orthogonal projection.
        loc = glGetUniformLocation(program, "typeOfProjection")
        glUniform1i(loc, 2)

        '''
     * This function clears any transformations, setting the values to the
     * defaults: no scaling (scale factor of 1), no rotation (degree of
     * rotation = 0), and no translation (0 translation in each direction).
     *
     * You will need to write this function, and maintain all of the values
     * which must be sent to the vertex shader.
     *
     * @param program - The ID of an OpenGL (GLSL) shader program to which
     *    parameter values are to be sent
    '''
    def clearTransform(self, program):
        #In this function, we set the scaling rotation and translate lists to
		#the default values
        scale = [1.0, 1.0, 1.0]
        rotation = [0.0, 0.0, 0.0]
        translate = [0.0, 0.0, 0.0]
        sloc = 0
        rloc = 0
        tloc = 0

        #we get the vectors scale, rotate and translate from shader.vert and
		#set it values to have the transformations to default values.

        sloc = glGetUniformLocation(program, "scale")
        rloc = glGetUniformLocation(program, "rotate")
        tloc = glGetUniformLocation(program, "translate")

        glUniform3fv(sloc, 1, scale, 0)
        glUniform3fv(rloc, 1, rotation, 0)
        glUniform3fv(tloc, 1, translate, 0)
        '''
     * This function sets up the transformation parameters for the vertices
     * of the teapot.  The order of application is specified in the driver
     * program.
     *
     * You will need to write this function, and maintain all of the values
     * which must be sent to the vertex shader.
     *
     * @param program - The ID of an OpenGL (GLSL) shader program to which
     *    parameter values are to be sent
     * @param xScale - amount of scaling along the x-axis
     * @param yScale - amount of scaling along the y-axis
     * @param zScale - amount of scaling along the z-axis
     * @param xRotate - angle of rotation around the x-axis, in degrees
     * @param yRotate - angle of rotation around the y-axis, in degrees
     * @param zRotate - angle of rotation around the z-axis, in degrees
     * @param xTranslate - amount of translation along the x axis
     * @param yTranslate - amount of translation along the y axis
     * @param zTranslate - amount of translation along the z axis
    '''
    def setUpTransform(self, program, xScale, yScale, zScale,
                        xRotate, yRotate, zRotate,
                        xTranslate, yTranslate, zTranslate):
        #we create a list for scaling, rotation and translation and
		#then set the vectors accordingly into the vectors that hold the
		#scaling, rotational and translation details in shader.vert.

        scale = [xScale, yScale, zScale]
        rotation = [xRotate, yRotate, zRotate]
        translate = [xTranslate, yTranslate, zTranslate]
        sloc = 0
        rloc = 0
        tloc = 0

        sloc = glGetUniformLocation(program, "scale")
        rloc = glGetUniformLocation(program, "rotate")
        tloc = glGetUniformLocation(program, "translate")

        glUniform3fv(sloc, 1, scale, 0)
        glUniform3fv(rloc, 1, rotation, 0)
        glUniform3fv(tloc, 1, translate, 0)
        '''
     * This function clears any changes made to camera parameters, setting the
     * values to the defaults: eyepoint (0.0,0.0,0.0), lookat (0,0,0.0,-1.0),
     * and up vector (0.0,1.0,0.0).
     *
     * You will need to write this function, and maintain all of the values
     * which must be sent to the vertex shader.
     *
     * @param program - The ID of an OpenGL (GLSL) shader program to which
     *    parameter values are to be sent
    '''
    def clearCamera(self, program):
        #We set the camera position to default values in the shader.vert file
        eye = [0.0, 0.0, 0.0]
        lookat = [0.0, 0.0, -1.0]
        up = [0.0, 1.0, 0.0]

        eloc = 0
        lloc = 0
        uloc = 0

        eloc = glGetUniformLocation(program, "eye")
        lloc = glGetUniformLocation(program, "look")
        uloc = glGetUniformLocation(program, "up")

        glUniform3fv(eloc, 1, eye, 0)
        glUniform3fv(lloc, 1, lookat, 0)
        glUniform3fv(uloc, 1, up, 0)
        '''
     * This function sets up the camera parameters controlling the viewing
     * transformation.
     *
     * You will need to write this function, and maintain all of the values
     * which must be sent to the vertex shader.
     *
     * @param program - The ID of an OpenGL (GLSL) shader program to which
     *    parameter values are to be sent
     * @param eyepointX - x coordinate of the camera location
     * @param eyepointY - y coordinate of the camera location
     * @param eyepointZ - z coordinate of the camera location
     * @param lookatX - x coordinate of the lookat point
     * @param lookatY - y coordinate of the lookat point
     * @param lookatZ - z coordinate of the lookat point
     * @param upX - x coordinate of the up vector
     * @param upY - y coordinate of the up vector
     * @param upZ - z coordinate of the up vector
    '''
    def setUpCamera(self, program, eyePointX, eyePointY, eyePointZ,
                    lookatX, lookatY, lookatZ,
                    upX, upY, upZ):
        #We create a list of eye, lookat and up values and then set these in
		#the shader.vert accordingly so that, we will have the camera position
		#set to the values we want.

        eye = [eyePointX, eyePointY, eyePointZ]
        lookat = [lookatX, lookatY, lookatZ]
        up = [upX, upY, upZ]

        eloc = 0
        lloc = 0
        uloc = 0
        eloc = glGetUniformLocation(program, "eye")
        lloc = glGetUniformLocation(program, "look")
        uloc = glGetUniformLocation(program, "up")

        glUniform3fv(eloc, 1, eye, 0)
        glUniform3fv(lloc, 1, lookat, 0)
        glUniform3fv(uloc, 1, up, 0)



