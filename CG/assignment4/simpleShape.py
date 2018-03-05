'''
Created on Nov 4, 2014

@author: Srinivas
'''
from numpy import array, int16, int32 

class simpleShape(object):
    '''
    classdocs
    '''
    points = []
    elements = []
    nverts = 0    
    
    

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def addTriangle(self,x0,y0,z0,x1,y1,z1,x2,y2,z2):
        
        self.points.append(x0)
        self.points.append(y0)
        self.points.append(z0)
        self.points.append(1.0)
        self.elements.append(self.nverts)
        self.nverts += 1
        
        self.points.append(x1)
        self.points.append(y1)
        self.points.append(z1)
        self.points.append(1.0)
        self.elements.append(self.nverts)
        self.nverts += 1
        
        self.points.append(x2)
        self.points.append(y2)
        self.points.append(z2)
        self.points.append(1.0)
        self.elements.append(self.nverts)
        self.nverts += 1

        
    def clear(self):
        self.nverts= 0
        self.points = []
        self.elements = []
    
    def getVertices(self):
        #value = array(self.points, dtype ='float32')
        #print self.points
        return array(self.points, dtype ='float32')
        
    def getElements(self):
        return array(self.elements, dtype = 'int16')
        
    def getNVerts(self):
        return int32(self.nverts)
            
