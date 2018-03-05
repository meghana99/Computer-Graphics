'''
Created on June 12, 2016

@author:
         Meghana Sathish (mxs7620@rit.edu)

Program to implement Mid point line algorithm and draw the initials of my name.

'''


class Rasterization(object):

    scan_line = 0

    def __init__(self,n):
        self.scan_line = n


    def drawLine(self, x0, y0, x1, y1, sc):

        #Your code goes here (midpoint line drawing)
        # the statement below is included just to provide a clean compile.  It should be removed and repalced with your code.
        dx = abs(x1 - x0)                   #difference between end and initial points
        dy = abs(y1 - y0)
        x, y = x0, y0
        tx = -1 if x0 > x1 else 1
        ty = -1 if y0 > y1 else 1           # check slope value
        if dx > dy:
            er = dx / 2.0                   #error calculation
            while x != x1:
                sc.setPixel(x, y)           #draw pixel
                er -= dy
                if er < 0:
                    y += ty
                    er += dx
                x += tx
        else:
            er = dy / 2.0
            while y != y1:
                sc.setPixel(x, y)
                er -= dx
                if er < 0:
                    x += tx
                    er += dy
                y += ty
        sc.setPixel(x, y)

    def myInitials (self, sc):

        # use light blue (0.678, 0.847, 0.902) for initials

        # the letter 'M' in blue

        sc.setColor (0, 0, 255)                 #color set to blue
        self.drawLine(60, 560, 120,560,sc)      #horizontal line from left to right
        self.drawLine(60, 560, 60, 360, sc)     #vertical line from bottom to top
        self.drawLine(60, 360, 120, 360, sc)
        self.drawLine(120, 560, 120, 430, sc)
        self.drawLine(120, 360, 170, 400, sc)   #38 degree slope
        self.drawLine(120, 430, 170, 470, sc)
        self.drawLine(170, 400, 220, 360, sc)   #321 degree slope
        self.drawLine(170, 470, 220, 430, sc)
        self.drawLine(220, 360, 280, 360, sc)
        self.drawLine(220, 430, 220, 560, sc)
        self.drawLine(280, 360, 280, 560, sc)   #vertical line from top to bottom
        self.drawLine(280, 560, 220, 560, sc)   #horizontal line from right to left

        # the letter 'S' in blue

        self.drawLine(340, 560, 420, 560, sc)   #horizontal line from left to right
        self.drawLine(340, 560, 340, 530, sc)   #vertical line from bottom to top
        self.drawLine(340, 530, 400, 530, sc)
        self.drawLine(400, 530, 430, 510, sc)   #326 degree slope
        self.drawLine(430, 510, 430, 470, sc)
        self.drawLine(430, 470, 400, 450, sc)   #413 degree slope
        self.drawLine(400, 450, 370, 450, sc)
        self.drawLine(370, 450, 340, 430, sc)   #213 degree slope
        self.drawLine(340, 430, 340, 390, sc)
        self.drawLine(340, 390, 370, 360, sc)   #315 degree slope
        self.drawLine(370, 360, 460, 360, sc)
        self.drawLine(420, 560, 460, 530, sc)   #323 degree slope
        self.drawLine(460, 530, 460, 460, sc)
        self.drawLine(460, 460, 420, 430, sc)   #216 degree slope
        self.drawLine(420, 430, 390, 430, sc)
        self.drawLine(390, 430, 370, 420, sc)   #206 degree slope
        self.drawLine(370, 420, 370, 400, sc)
        self.drawLine(370, 400, 390, 380, sc)   #315 degree slope
        self.drawLine(390, 380, 460, 380, sc)
        self.drawLine(460, 380, 460, 360, sc)
