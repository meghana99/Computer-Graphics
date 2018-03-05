'''
Created on June 12, 2016



Contibutor: Meghana Sathish
            mxs7620@rit.edu

This is a program to draw different color filled polygons using scan line fill algorithm.
'''


class Rasterization(object):

    scan_line = 0

    def __init__(self,n):
        self.scan_line = n

    '''
    Draw a filled polygon in the simpleCanvas sc.

    The polygon has n distinct vertices. The
    coordinates of the vertices making up the polygon are stored in the
    x and y lists.  The ith vertex will have coordinate  (x[i], y[i])

    You are to add the implementation here using only calls
    to sc.setPixel()
    '''

    def drawPolygon(self, n,x,y,sc):
        from matplotlib import path
        xy = [(x[i],y[i]) for i in range (0,n)] #vertices of the polygon
        print(xy)

        p = path.Path(xy) #converting them to an array
        print(p)
        min_x = min(x[0:n]) #minimum x value
        max_x = max(x[0:n]) #maximum x value
        min_y = min(y[0:n]) #minimum y value
        max_y = max(y[0:n]) #maximum y value

        for tx in range(min_x,max_x+1):
            for ty in range(min_y,max_y+1):
                if p.contains_points([(tx,ty)])[0]: #check if the path exists
                    sc.setPixel(tx,ty)      #if it exists then set pixel at that point


