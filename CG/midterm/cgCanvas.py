# midterm exam

# author : Meghana Sathish (mxs7620@rit.edu)



from simpleCanvas import simpleCanvas
import numpy as np
import math
import copy as copy
from clipper1 import clipper


class cgCanvas(simpleCanvas):
    vertices = []
    uniqueID = 0

    def __init__(self, w, h):
        self.setSize(w, h)

    def addPoly(self, x, y, n):
        '''

             addPoly - Adds and stores a polygon to the canvas.  Note that this method does not
                       draw the polygon, but merely stores it for later draw.  Drawing is
                       initiated by the draw() method.

                       Returns a unique integer id for the polygon.

            :param x - Array of x coords of the vertices of the polygon to be added.
            :param y - Array of y coords of the vertices of the polygon to be added.
            :param n - Number of vertices in polygon

            :return a unique integer identifier for the polygon
        '''
        self.uniqueID += 1
        add = []
        for i in range(n):
            add.append([x[i], y[i]])
        self.vertices.append(add)
        return self.uniqueID

    def clearTransform(self):
        '''
        clearTransform - sets the current transformation to be the identity
        '''
        m=np.zeros(shape=(3,3))
        m[0]=[1,0,0]
        m[1]=[0,1,0]
        m[2]=[0,0,1]
        self.matrix = m

    listx = []
    listy = []
    outx = []
    outy = []
    x_list = []
    y_list = []

    def drawPoly(self, polyID):
        # function to draw the polygon
        '''
        :param polyID: an unique ID returned for each polygon.
        :return:
        '''
        q = copy.deepcopy(self.vertices[polyID - 1])
        points = copy.deepcopy(q)
        self.listx = []
        self.listy = []
        for i in range(len(points)):
            self.listx.append(points[i][0])
            self.listy.append(points[i][1])

        olx = []
        oly = []

        for i in range(len(self.listx)):
            m = np.matrix([[self.listx[i]], [self.listy[i]], [1]])
            m = np.matmul(self.matrix, m)
            olx.append(m[0].item(0))
            oly.append(m[1].item(0))

        self.listx = olx
        self.listy = oly

        A = copy.deepcopy(self.listx)
        B = copy.deepcopy(self.listy)

        n = self.clipPolygon(len(points), self.listx, self.listy, self.listx, self.listy, self.llx, self.lly, self.urx,
                             self.ury)

        if n == 0:
            self.listx = copy.deepcopy(A)
            self.listy = copy.deepcopy(B)
            n = len(A)

        trans_matrix = np.matrix([[(self.x_max - self.x_min) / (self.urx - self.llx), 0,
                                   ((self.urx * self.x_min) - (self.lly * self.x_max)) / (self.urx - self.llx)],
                                  [0, (self.y_max - self.y_min) / (self.ury - self.lly),
                                   ((self.ury * self.y_min) - (self.lly * self.y_max)) / (self.ury - self.lly)],
                                  [0, 0, 1]])

        for i in range(n):
            m = np.matrix([[self.listx[i]], [self.listy[i]], [1]])
            m = np.matmul(trans_matrix, m)

            self.outx.append(int(m[0].item(0)))
            self.outy.append(int(m[1].item(0)))

        self.polygon(n, self.outx, self.outy, self)
        self.outy = []
        self.outx = []


    def rotate(self, degrees):
        '''
        :param degrees: degrees at which it is expected to rotate.
        :return:
        '''
        rotate_matrix = np.zeros(shape=(3, 3))
        rotate_matrix[0] = [math.cos(math.radians(degrees)), -math.sin(math.radians(degrees)), 0]
        rotate_matrix[1] = [math.sin(math.radians(degrees)), math.cos(math.radians(degrees)), 0]
        rotate_matrix[2] = [0, 0, 1]

        self.matrix = np.matmul(rotate_matrix,self.matrix)

    def scale(self, x, y):
        '''
        scale - Add a scale to the current transformation by premultiplying the appropriate
        scaling matrix to the current transformtion matrix.
        :param x - Amount of scaling in x.
        :param y - Amount of scaling in y.
        '''
        scale_matrix = np.zeros(shape=(3, 3))
        scale_matrix[0] = [x, 0, 0]
        scale_matrix[1] = [0, y, 0]
        scale_matrix[2] = [0, 0, 1]

        self.matrix = np.matmul(scale_matrix,self.matrix)

    def translate(self, x, y):
        '''
        translate - Add a translation to the current transformation by premultiplying the appropriate
        translation matrix to the current transformtion matrix.
        :param x - Amount of translation in x.
        :param y - Amount of translation in y.
        '''
        translate_matrix = np.zeros(shape=(3, 3))
        translate_matrix[0] = [1, 0, x]
        translate_matrix[1] = [0, 1, y]
        translate_matrix[2] = [0, 0, 1]

        self.matrix = np.matmul(translate_matrix,self.matrix)

    def setClipWindow(self, bottom, top, left, right):
        '''
        setClipWindow - defines the clip window
        :param bottom - y coord of bottom edge of clip window (in world coords)
        :param top - y coord of top edge of clip window (in world coords)
        :param left - x coord of left edge of clip window (in world coords)
        :param right - x coord of right edge of clip window (in world coords)
        '''
        self.llx = left
        self.lly = bottom
        self.urx = right
        self.ury = top

    def setViewport(self, x, y, width, height):
        """
        setViewport - defines the viewport
        :param xmin - x coord of lower left of view window (in screen coords)
        :param ymin - y coord of lower left of view window (in screen coords)
        :param width - width of view window (in world coords)
        :param height - width of view window (in world coords)

        """
        self.x_max = x + width
        self.x_min = x
        self.y_max = y + height
        self.y_min = y

    def clipPolygon(self, in1, inx, iny, outx, outy, llx, lly, urx, ury):
        n_out = 0
        # YOUR IMPLEMENTATION GOES HERE
        import math
        from matplotlib import path
        clipping_rectangle_vertices = [[llx, lly], [urx, lly], [urx, ury],
                                       [llx, ury]]  # creating set of vertices of clip rectangle

        clipping_rectangle = path.Path(clipping_rectangle_vertices)  # creating array
        inx = copy.deepcopy(inx)
        iny = copy.deepcopy(iny)
        outx.clear()
        outy.clear()
        edges = [[[llx, lly], [urx, lly]], [[urx, lly], [urx, ury]], [[urx, ury], [llx, ury]],
                 [[llx, ury], [llx, lly]]]  # creating set of edges of clip rectangle

        points = [(inx[i], iny[i]) for i in range(0, in1)]
        points.append((inx[0], iny[0]))  # storing input vertices in a list

        for i in range(0, len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            edge2 = [p1, p2]

            if clipping_rectangle.contains_points([p1])[
                0]:  # conditions to check if the polgon points lie on the clipping rectangle
                outx.append(p1[0])
                outy.append(p1[1])

                if clipping_rectangle.contains_points([p2])[0]:
                    outx.append(p2[0])
                    outy.append(p2[1])
                else:
                    intersection_points = []
                    for edge in edges:
                        p = self.intersection(edge, edge2)
                        if p is not None:
                            if p not in intersection_points:
                                intersection_points.append(p)

                    for point in intersection_points:
                        outx.append(point[0])
                        outy.append(point[1])
            elif clipping_rectangle.contains_points([p2])[0]:

                intersection_points = []
                for edge in edges:
                    p = self.intersection(edge, edge2)
                    if p is not None:
                        if p not in intersection_points:
                            intersection_points.append(p)

                for point in intersection_points:
                    outx.append(point[0])
                    outy.append(point[1])
                outx.append(p2[0])
                outy.append(p2[1])
            else:
                min_dist_vertex = (llx, lly)
                min_dist = 999999999
                for edge in edges:
                    dist = math.hypot(p2[0] - edge[0][0], p2[1] - edge[0][1])
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_vertex = (edge[0][0], edge[0][1])
                    dist = math.hypot(p2[0] - edge[1][0], p2[1] - edge[1][1])
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_vertex = (edge[1][0], edge[1][1])
                    dist = math.hypot(p1[0] - edge[0][0], p1[1] - edge[0][1])
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_vertex = (edge[0][0], edge[0][1])
                    dist = math.hypot(p1[0] - edge[1][0], p1[1] - edge[1][1])
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_vertex = (edge[1][0], edge[1][1])
                outx.append(min_dist_vertex[0])
                outy.append(min_dist_vertex[1])
        self.listx = []
        self.listy = []
        self.listx = outx
        self.listy = outy
        n_out = len(outy)
        return n_out

    def intersection(self, l1, l2):  # find the difference between two lines and the delta value
        x = (l1[0][0] - l1[1][0], l2[0][0] - l2[1][0])
        y = (l1[0][1] - l1[1][1], l2[0][1] - l2[1][1])

        def delta(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = delta(x, y)
        if div == 0:
            return None

        d = (delta(*l1), delta(*l2))
        x = delta(d, x) / div
        y = delta(d, y) / div

        min_x = min(l2[0][0], l2[1][0])
        min_y = min(l2[0][1], l2[1][1])

        max_x = max(l2[0][0], l2[1][0])
        max_y = max(l2[0][1], l2[1][1])

        if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
            return (x, y)
        else:
            return None

    def polygon(self, n, x, y, sc):
        # the code used to draw the polygon.
        from matplotlib import path
        xy = [(x[i]-1 if x[i]-1 >= 0 else 0, y[i]-1 if y[i]-1 >=0 else 0) for i in range(0, n)]  # vertices of the polygon

        p = path.Path(xy)  # converting them to an array
        min_x = min(x[0:n])  # minimum x value
        max_x = max(x[0:n])  # maximum x value
        min_y = min(y[0:n])  # minimum y value
        max_y = max(y[0:n])  # maximum y value

        for tx in range(min_x, max_x + 1):
            for ty in range(min_y, max_y + 1):
                if p.contains_points([(tx, ty)])[0]:  # check if the path exists
                    sc.setPixel(tx, ty)  # if it exists then set pixel at that point
