# Clipper.py
#
# Created on June 12, 2016
#
#
# Contributor:  Meghana Sathish (mxs7620@rit.edu)
# Implentation of Sutherland Hodgman algorithm for polygon clipping
# 
# Object for performing clipping

class clipper(object):



    #   clipPolygon
    #
    #   Clip the polygon with vertex count in and vertices inx/iny
    #   against the rectangular clipping region specified by lower-left corner
    #   (llx,lly) and upper-right corner (urx,ury). The resulting vertices are
    #   placed in outx/outy.
    #
    #   The routine should return the with the vertex count of polygon
    #   resultinhg from the clipping.
    #
    #   @param in the number of vertices in the polygon to be clipped
    #   @param inx - x coords of vertices of polygon to be clipped.
    #   @param iny - y coords of vertices of polygon to be clipped.
    #   @param outx - x coords of vertices of polygon resulting after clipping.
    #   @param outy - y coords of vertices of polygon resulting after clipping.
    #   @param llx - x coord of lower left of clipping rectangle.
    #   @param lly - y coord of lower left of clipping rectangle.
    #   @param urx - x coord of upper right of clipping rectangle.
    #   @param ury - y coord of upper right of clipping rectangle.
    #
    #   @return number of vertices in the polygon resulting after clipping

    def clipPolygon(self, in1, inx, iny, outx, outy, llx, lly, urx, ury):
        n_out = 0
        # YOUR IMPLEMENTATION GOES HERE
        import math
        from matplotlib import path
        clipping_rectangle_vertices = [[llx, lly], [urx, lly], [urx, ury], [llx, ury]] #creating set of vertices of clip rectangle

        clipping_rectangle = path.Path(clipping_rectangle_vertices) #creating array

        outx.clear()
        outy.clear()

        edges = [[[llx, lly], [urx, lly]], [[urx, lly], [urx, ury]], [[urx, ury], [llx, ury]],
                 [[llx, ury], [llx, lly]]] #creating set of edges of clip rectangle

        points = [(inx[i], iny[i]) for i in range(0, in1)]
        points.append((inx[0], iny[0])) #storing input vertices in a list

        for i in range(0, len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            edge2 = [p1, p2]

            if clipping_rectangle.contains_points([p1])[0]: #conditions to check if the polgon points lie on the clipping rectangle
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
        n_out = len(outy)
        return n_out

    def intersection(self, l1, l2): # find the difference between two lines and the delta value
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
