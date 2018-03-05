'''
//  pyramid.py
//
//  Routines for tessellating a standard pyramid.
//
//  Students should not be modifying this file.
//
//  @author Srini
'''

from simpleShape import simpleShape

class pyramid(simpleShape):

    #vertices of the pyramid
    pyramidVertices = [ -0.917525, 0.080591, -0.887614, -0.099281, 0.080591, -0.069369,
			-0.917525, 0.080591, -0.069370, -0.507979, 0.898835, -0.478067, -0.508828, 0.898835, -0.478916,
			-0.508828, 0.898835, -0.478067, -0.099281, 0.080591, -0.887614, -0.507979, 0.898835, -0.478916]

    #find the number of vertices
    pyramidVerticesLength = len(pyramidVertices)


#
# Each group of three values specifies a pyramid vertex normal
#
    pyramidNormals = [ -0.0000, -1.0000, 0.0000, 0.0000, 1.0000, 0.0000, -0.8946, 0.4468,
			-0.0000, 0.0000, 0.4468, -0.8946, 0.8946, 0.4468, -0.0000, 0.8946, 0.4469, -0.0000, -0.0000,
			0.4468, 0.8946 ]

    #find the number of normals
    pyramidNormalsLength = len (pyramidNormals)
    
    #
    # Each group of three entries specifies a triangle for the pyramid
    #
    pyramidElements = [1, 2, 3, 4, 5, 6, 6, 1, 3, 5, 7, 1, 7, 4, 2, 3, 4, 6, 1, 7, 2, 4, 8, 5, 6,
			5, 1, 5, 8, 7, 7, 8, 4, 3, 2, 4 ]

    #find the number of pyramid elements
    pyramidElementsLength = len(pyramidElements)
        
        #
        # Each group of three entries specifies the normals used to create
        # a single averaged pyramid vertex normal
        #
    pyramidNormalIndices = [ 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 5, 7, 7, 7, 1, 1, 1, 2, 2, 2,
			3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7 ]
            
    pyramidNormalIndicesLength = len(pyramidNormalIndices)

    def makePyramid(self):

        for i in range(0, self.pyramidElementsLength-2, 3):
            # calculate the base indices of the three vertices
            point1 = 3 * (self.pyramidElements[i] - 1);  # slots 0, 1, 2
            point2 = 3 * (self.pyramidElements[i+1] - 1);  # slots 0, 1, 2
            point3 = 3 * (self.pyramidElements[i+2] - 1);  # slots 0, 1, 2

            normal1 = 3 * (self.pyramidNormalIndices[i] - 1);  # slots 0, 1, 2
            normal2 = 3 * (self.pyramidNormalIndices[i+1] - 1);  # slots 0, 1, 2
            normal3 = 3 * (self.pyramidNormalIndices[i+2] - 1);  # slots 0, 1, 2

            self.addTriangleWithNorms(self.pyramidVertices[point1 + 0], self.pyramidVertices[point1 + 1],
                                      self.pyramidVertices[point1 + 2], self.pyramidVertices[point2 + 0],
                                      self.pyramidVertices[point2 + 1], self.pyramidVertices[point2 + 2],
                                      self.pyramidVertices[point3 + 0], self.pyramidVertices[point3 + 1],
                                      self.pyramidVertices[point3 + 2], self.pyramidNormals[normal1 + 0],
                                      self.pyramidNormals[normal1 + 1], self.pyramidNormals[normal1 + 2],
                                      self.pyramidNormals[normal2 + 0], self.pyramidNormals[normal2 + 1],
                                      self.pyramidNormals[normal2 + 2], self.pyramidNormals[normal3 + 0],
                                      self.pyramidNormals[normal3 + 1], self.pyramidNormals[normal3 + 2])
            


        
    def __init__(self):
        pass

 
