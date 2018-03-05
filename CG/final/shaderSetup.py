'''

@author: Meghana Sathish(mxs7620@rit.edu)
'''

from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class shaderSetup(object):
    '''
    classdocs
    '''

    program = None

    #constructor
    def __init__(self, params):
        '''
        Constructor
        '''
        
    def textFileRead(self, fileName):
        '''
        @:param: filename is the name of the file
        This function is used to read the file.
        '''
        try:
            file_handle = open(fileName)
            file_data = file_handle.read()
            file_handle.close()
            return file_data
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
     
    def printShaderInfoLog(self, shaderObj, shaderType):
        '''
        This function is prints the information of the shader.
        :param shaderObj: An object of the shader being passed
        :param shaderType: Type of the shader
        :return: Exception raised if not a proper shader.
        '''
        
        log_length = GLint()
        
        if glIsShader(shaderObj):
            glGetShaderiv(shaderObj, GL_INFO_LOG_LENGTH, log_length)
        else:
            print('Not a Shader Error: ')
            raise Exception('Not a Shader Error')
        
        log = glGetShaderInfoLog(shaderObj)
        if log: 
            print('Shader Syntax Error: ',shaderType, log)
            raise Exception('Shader Syntax Error', log)
        
    def printProgramInfoLog(self,programObj):
        '''
        Function to print log information of program.
        :param programObj: An object of the program
        :return: Exception raised if the program has error.
        '''
        log_length = GLint()
        
        if glIsProgram(programObj):
            glGetProgramiv(programObj, GL_INFO_LOG_LENGTH, log_length)
        else:
            print('Not a program Error: ')
            raise Exception('Not a Program Error')
            
        log = glGetProgramInfoLog(programObj)
        
        if log: 
            print('Program Error: ', log)
            raise Exception('Program Error', log)   
            

    def readAndCompile(self, vertFileName, fragFileName):
        '''
        Function to read and compile the shader files
        :param vertFileName: Vertex file of the shader
        :param fragFileName: Fragment file of the shader
        :return: programID
        '''

        if bool(glCreateShader(GL_VERTEX_SHADER)):
            vs = glCreateShader(GL_VERTEX_SHADER)
        else:
            vs =""
            print("something seriously wrong here")
        fs = glCreateShader(GL_FRAGMENT_SHADER)
        
        vs_source = self.textFileRead(vertFileName)
        fs_source = self.textFileRead(fragFileName)
        
        glShaderSource(vs, vs_source)
        glShaderSource(fs, fs_source)
        
        #Compile the Shader
        glCompileShader(vs)
        self.printShaderInfoLog(vs,'vertex')
        glCompileShader(fs)
        self.printShaderInfoLog(fs,'fragment')
        
        self.program  = glCreateProgram()
        
        glAttachShader(self.program, vs)
        glAttachShader(self.program, fs)
        glLinkProgram(self.program)
        
        self.printProgramInfoLog(self.program)
        
        return self.program
                    
                