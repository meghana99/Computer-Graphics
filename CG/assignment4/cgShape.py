'''
Created on Aug 4, 2016

@author: Srinivas
contributor: Meghana Sathish (mxs7620)

Program to implement triangular tessellation for the basic shapes
like cube, cylinder, cone and sphere.
'''

from math import cos, sin, radians
from numpy import arange,float32,float128
from simpleShape import simpleShape
import math

class cgShape(simpleShape):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    #
    # makeCube - Create a unit cube, centered at the origin, with a given number
    # of subdivisions in each direction on each face.
    #
    # @param subdivision - number of equal subdivisions to be made in each
    #        direction along each face
    #
    # Can only use calls to addTriangle()
    #
    def makeCube(self,subdivisions):
        
        if(subdivisions < 1):
            subdivisions = 1
        # add your code here

        # the loop here is to divide the cube horizontally.
        for i in range(0,subdivisions):
            #intermediate values of the horizontal slices.
            m0 = (float(i) / subdivisions) - 0.5
            m1 = (float(i+1) / subdivisions) - 0.5
            # this loop for dividing the cube vertically
            for j in range(0,subdivisions):
                #intermediate values of the vertical slices.
                n0 = (float(j) / subdivisions) - 0.5
                n1 = (float(j+1) / subdivisions) - 0.5
                #make calls to the addTriangle function
                # z constant
                self.addTriangle(m1, n1, 0.5, m0, n1, 0.5, m0, n0, 0.5)
                self.addTriangle(m0, n0, 0.5, m1, n0, 0.5, m1, n1, 0.5)
                # x constant
                self.addTriangle(0.5, m1, n1, 0.5, m0, n1, 0.5, m0, n0)
                self.addTriangle(0.5, m0, n0, 0.5, m1, n0, 0.5, m1, n1)
                # z constant
                self.addTriangle(m0, n1, -0.5, m1, n1, -0.5, m1, n0, -0.5)
                self.addTriangle(m1, n0, -0.5, m0, n0, -0.5, m0, n1, -0.5)
                # x constant
                self.addTriangle(-0.5, m1, n0, -0.5, m0, n0, -0.5, m0, n1)
                self.addTriangle(-0.5, m0, n1, -0.5, m1, n1, -0.5, m1, n0)
                # y constant
                self.addTriangle(n0, 0.5, m1, n1, 0.5, m1, n1, 0.5, m0)
                self.addTriangle(n1, 0.5, m0, n0, 0.5, m0, n0, 0.5, m1)
                # y constant
                self.addTriangle(n0, -0.5, m0, n1, -0.5, m0, n1, -0.5, m1)
                self.addTriangle(n1, -0.5, m1, n0, -0.5, m1, n0, -0.5, m0)

    # makeCylinder - Create polygons for a cylinder with unit height, centered at
    # the origin, with separate number of radial subdivisions and height
    # subdivisions.
    #
    # @param radius - Radius of the base of the cylinder
    # @param radialDivision - number of subdivisions on the radial base
    # @param heightDivisions - number of subdivisions along the height
    #
    # Can only use calls to addTriangle()
    #
    def makeCylinder(self,radius,radialdivision,heightdivision):
        
        
        if(radialdivision < 3):
            radialdivision = 3;
            
        if(heightdivision < 1):
            heightdivision = 1


        ia = float(math.pi) * 2
        z = self.drange(0.0, ia, ia / radialdivision)
        # to create the base of the cylinder
        for angle in z:
            angle += ia / radialdivision
            x = radius * math.cos(math.pi - angle)
            y = radius * math.sin(math.pi - angle)
            p = radius * math.cos(math.pi - (angle + (ia / radialdivision)))
            w = radius * math.sin(math.pi - (angle + (ia / radialdivision)))
            #top of cylinder
            self.addTriangle(0, 0.5, 0, float(x), 0.5, float(y), float(p), 0.5, float(w))
            # bottom of cylinder
            self.addTriangle(0, -0.5, 0, float(p),-0.5, float(w),float(x), -0.5, float(y))
            # draw surface of the cylinder
            for j in range(0,heightdivision):
                m0 = (float(j) / heightdivision) - 0.5
                m1 = (float(j + 1) / heightdivision) - 0.5
                self.addTriangle(float(p), m1, float(w), float(x), m1, float(y), float(x), m0, float(y))
                self.addTriangle(float(x), m0, float(y), float(p), m0, float(w), float(p), m1, float(w))


    def drange(self,start,stop,step):
        '''
        function for for loop which takes in floating point numbers
        @:param start - the start value of the loop
        @:param stop - the end value of the loop
        @:param step - the increment in the loop
        '''
        i=0
        while start + i *step <stop:
            yield start + i * step
            i += 1
    #
    # makeCone - Create polygons for a cone with unit height, centered at the
    # origin, with separate number of radial subdivisions and height
    # subdivisions.
    #
    # @param radius - Radius of the base of the cone
    # @param radialDivision - number of subdivisions on the radial base
    # @param heightDivisions - number of subdivisions along the height
    #
    # Can only use calls to addTriangle()
    #
    def makeCone(self, radius, radialdivision, heightdivision):

        if(radialdivision < 3):
            radialdivision = 3
        if (heightdivision < 1):
            heightdivision = 1

        ia = float(math.pi) * 2

        z = self.drange(0.0,ia,ia/radialdivision)

        for angle in z:
            x1 = float((radius * math.cos(math.pi - angle)))
            x2 = float((radius * math.cos(math.pi - (angle + (ia / radialdivision)))))
            z1 = float((radius * math.sin(math.pi - angle)))
            z2 = float((radius * math.sin(math.pi - (angle + (ia / radialdivision)))))
            # To draw the circular base of the cone
            self.addTriangle(0, 0.5, 0, x1, 0.5, z1, x2, 0.5, z2)
            # Calculate the intermediate points on the surface so that the tessellation is maintained.
            px1 = x1 / heightdivision
            px2 = x2 / heightdivision
            pz1 = z1 / heightdivision
            pz2 = z2 / heightdivision
            factor = 1.0 / heightdivision
            y = 0.5
            for j in range(0,heightdivision):
                self.addTriangle(x1, y, z1, x1 - px1, y - factor, z1 - pz1, x2, y, z2)
                self.addTriangle(x2, y, z2, x1 - px1, y - factor, z1 - pz1, x2 - px2, y - factor, z2 - pz2)
                y = y - factor
                x1 = x1 - px1
                x2 = x2 - px2
                z1 = z1 - pz1
                z2 = z2 - pz2
    #
    # makeSphere - Create sphere of a given radius, centered at the origin,
    # using spherical coordinates with separate number of thetha and
    # phi subdivisions.
    #
    # @param radius - Radius of the sphere
    # @param slices - number of subdivisions in the theta direction
    # @param stacks - Number of subdivisions in the phi direction.
    #
    # Can only use calls to addTriangle()
    #
    def makeSphere(self,radius, slices, stacks):
    
        # IF DOING RECURSIVE SUBDIVISION:
        # use a minimum value of 1 instead of 3
        # add an 'else' clause to set a maximum value of 5
        if(slices < 3):
            slices = 3

        if(stacks < 3):
            stacks = 3

        # Iterate through each value of stack and slice and calculate the value
		#of theta1, theta2, phi1 and phi2. Then we calculate the x,y and z
		#coordinates values using the formula x = r*cos(theta)sin(phi), y =
		# r*sin(theta)sin(phi) and z = r*cos(phi) for all the a,b,c,d where
		# a,b,c,d are the intermediate values of the sphere.

        for i in range(0,stacks):
            phi1 = float(i) / stacks * float(math.pi)
            phi2 = float(i + 1) / stacks * float(math.pi)
            for j in range(0,slices):
                theta1 = float(j) / slices * float(float128(2.0) * math.pi)
                theta2 = float(j + 1) / slices * float(float128(2.0) * math.pi)
                ax = radius * float(math.cos(theta1)) * float(math.sin(phi1))
                ay = radius * float(math.sin(theta1)) * float(math.sin(phi1))
                az = radius * float(math.cos(phi1))
                bx = radius * float(math.cos(theta2)) * float(math.sin(phi1))
                by = radius * float(math.sin(theta2)) * float(math.sin(phi1))
                bz = radius * float(math.cos(phi1))
                cx = radius * float(math.cos(theta1)) * float(math.sin(phi2))
                cy = radius * float(math.sin(theta1)) * float(math.sin(phi2))
                cz = radius * float(math.cos(phi2))
                dx = radius * float(math.cos(theta2)) * float(math.sin(phi2))
                dy = radius * float(math.sin(theta2)) * float(math.sin(phi2))
                dz = radius * float(math.cos(phi2))
                # call addTriangle to make triangles of the calculated values
                self.addTriangle(bx, by, bz, ax, ay, az, cx, cy, cz)
                self.addTriangle(cx, cy, cz, dx, dy, dz, bx, by, bz)