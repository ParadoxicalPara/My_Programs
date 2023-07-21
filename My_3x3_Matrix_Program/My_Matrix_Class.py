# Author: Paradoxical
from button import button
from graphics import *
from math import gcd
def main():
    win = drawGraphics()
    # Creating buttons and activating some
    transBtn = button(Point(6,1.5), 2, 1, "Transpose", win)
    adjBtn = button(Point(9,1.5), 2, 1, "Adjoint", win)
    detBtn = button(Point(12,1.5), 2, 1, "Determinant", win)
    invBtn = button(Point(15,1.5), 2, 1, "Inverse", win)
    exitBtn = button(Point(1,0.5), 1, 0.5, "Exit", win)
    exitBtn.animate()
    exitBtn.activate()
    inEntries = entry(Point(4,5), win)
    inMatrix = matrix()
    result = text(Point(17,5),win)
    while True:
        """Checking if entries are filled with only numbers so that it can
activate the needed buttons to perform the operations on it. Incase the
entries are not entirely filled with numbers,"""
        if inEntries.isFull():
            transBtn.activate()
            adjBtn.activate()
            detBtn.activate()
            invBtn.activate()
        else:
            transBtn.deactivate()
            adjBtn.deactivate()
            detBtn.deactivate()
            invBtn.deactivate()
        """Checking if a button is clisked so operations can be
performed be performed on the numbers in the entries. Incase the button is
deactivated, the operation will not be executed"""
        click = win.checkMouse()
        if click:
            if exitBtn.clicked(click):
                exitBtn.animate()
                break
            elif transBtn.clicked(click):
                transBtn.animate()
                inMatrix.update(inEntries.Entries())
                result.update(inMatrix.transpose())
            elif adjBtn.clicked(click):
                adjBtn.animate()
                inMatrix.update(inEntries.Entries())
                result.update(inMatrix.adjoint())
            elif detBtn.clicked(click):
                detBtn.animate()
                inMatrix.update(inEntries.Entries())
                result.updateText(inMatrix.determinant())
            elif invBtn.clicked(click):
                invBtn.animate()
                inMatrix.update(inEntries.Entries())
                result.update(inMatrix.inverse())
    win.close()
#-------Graphics Window Design-------------------   
def drawGraphics():
    win = GraphWin("Matrix (3x3)", 1000, 500)
    win.setCoords(0.0,0.0,20.0,10.0)
    win.setBackground(color_rgb(252,222,103))
    inRect = drawRect(Point(4,5), 3.5, 3.5, win)
    outRect = drawRect(Point(17,5), 3.5,3.5, win)
    inpTxt = drawTxt(Point(1.5, 7.4), "Input:", win)
    outTxt = drawTxt(Point(14.5,7.4), "Output:", win)
    return win
def drawRect(pt, width, height, win):
    x1, y1 = pt.getX()+width/2, pt.getY()+height/2
    x2, y2 = pt.getX()-width/2, pt.getY()-height/2
    rect = Rectangle(Point(x1,y1), Point(x2,y2))
    rect.setWidth(2)
    rect.draw(win)
    return rect
def drawTxt(pt, label, win):
    txt = Text(pt, label)
    txt.setSize(10)
    txt.draw(win)
    return txt
#-------------Entries and Texts---------------------
class text:
    """This takes a center point for texts of a 3x3 matrix of the form:
|a b c|
|d e f|
|g h i|
on window \"win\""""
    def __init__(self, centerPoint, win):
        self.win = win
        x, y = centerPoint.getX(), centerPoint.getY()
        a,b,c,d,e,f,g,h,i = self.drawText(Point(x-1,y+1),"", self.win), \
                      self.drawText(Point(x,y+1),"", self.win), \
                      self.drawText(Point(x+1,y+1),"", self.win), \
                     self.drawText(Point(x-1,y),"", self.win), \
                      self.drawText(Point(x,y),"", self.win), \
                      self.drawText(Point(x+1,y),"", self.win), \
                     self.drawText(Point(x-1,y-1),"", self.win), \
                      self.drawText(Point(x,y-1),"", self.win), \
                      self.drawText(Point(x+1,y-1),"", self.win)
        self.txts= [[a,b,c], [d,e,f], [g,h,i]]
    def drawText(self, pt, label, win):
        txt = Text(pt, label)
        txt.setSize(12)
        txt.draw(win)
        return txt
    def clear(self):
        """Clears the texts from the window"""
        for i in range(3):
            for j in range(3):
                self.txts[i][j].setText("")
    def __repr__(self):
        return self.txts
    def update(self, Matrix):
        """Changes texts to those in the matrix 'Matrix'"""
        for i in range(3):
            for j in range(3):
                self.txts[i][j].setText("{}".format(Matrix[i][j]))
    def updateText(self, text):
        """Updates the value of a single text on the screen"""
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    self.txts[i][j].setText("")
                else:
                    self.txts[i][j].setText("{}".format(text))
class entry:
    """This takes a center point for entries of a 3x3 matrix of the form:
|T1 T2 T3|
|T4 T5 T6|
|T7 T8 T9|
on window \"win\""""
    def __init__(self, centerPoint, win):
        self.win = win
        x, y = centerPoint.getX(), centerPoint.getY()
        self.entries = [[self.drawEntry(Point(x-1,y+1), self.win), \
                      self.drawEntry(Point(x,y+1), self.win), \
                      self.drawEntry(Point(x+1,y+1), self.win)], \
                     [self.drawEntry(Point(x-1,y), self.win), \
                      self.drawEntry(Point(x,y), self.win), \
                      self.drawEntry(Point(x+1,y), self.win)], \
                     [self.drawEntry(Point(x-1,y-1), self.win), \
                      self.drawEntry(Point(x,y-1), self.win), \
                      self.drawEntry(Point(x+1,y-1), self.win)]]
        
    def drawEntry(self, pt, win):
        ent = Entry(pt, 3)
        ent.setFill("white")
        ent.draw(win)
        return ent
    def Entries(self):
        """Returns the values in the entries"""
        rtnEntry = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                rtnEntry[i][j] = int(self.entries[i][j].getText())
        return rtnEntry
    def isFull(self):
        """Checks whether there are values in all the entries are floats"""
        try:
            for row in self.entries:
                for column in row:
                    int(column.getText())
            return True
        except ValueError:
            return False

        
class matrix:
    """This takes input for a 3x3 matrix in the form:
|a b c|
|d e f|
|g h i|"""
    def __init__(self, listOfNums=[[0,0,0],[0,0,0],[0,0,0]]):
        self.mat = listOfNums
    def update(self, listOfNums):
        """Updates the matrix to the elements in listOfNums"""
        self.mat = listOfNums
    def determinant(self, Matrix=None):
        """Returns the determinant of matrix"""
        Matrix = Matrix or self.mat
        return Matrix[0][0]*self.cofactor(0,0,Matrix) \
                 + Matrix[0][1]*self.cofactor(0,1,Matrix) \
                 + Matrix[0][2]*self.cofactor(0,2,Matrix)
    def transpose(self, Matrix=None):
        """Returns the transpose of matrix"""
        Matrix = Matrix or self.mat
        result = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                result[i][j] = Matrix[j][i]
        return result
    def adjoint(self, Matrix=None):
        """Returns the adjoint of matrix"""
        Matrix = Matrix or self.mat
        result = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                result[i][j] = self.cofactor(i,j,Matrix)
        result = self.transpose(result)
        return result
    def inverse(self, Matrix=None):
        """Returns the inverse of a matrix"""
        Matrix = Matrix or self.mat
        result = self.adjoint(Matrix)
        det = self.determinant(Matrix)
        if det==0:
            return [["","No inverse",""],["","because"\
                                ,""],["","determinat is: 0",""]]
        else:
            for i in range(3):
                for j in range(3):
                    result[i][j] = self.reduceFrac(result[i][j], det)
            return result
    def cofactor(self, row, column, Matrix):
        [[a,b,c], [d,e,f], [g,h,i]] = Matrix
        mat = [[a,b,c], [d,e,f], [g,h,i]]
        mat.pop(row)
        mat[0].pop(column)
        mat[1].pop(column)
        result = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        if (column+row)%2 == 0:
            return result
        else:
            return -result
    def reduceFrac(self, numerator, denominator):
        if denominator == 0:
            return ValueError
        elif numerator%denominator==0:
            return numerator//denominator
        else:
            if (numerator<0 and denominator>0) or \
               (numerator>0 and denominator<0):
                sign = "-"
            else:
                sign = ""
            return "{0}{1}/{2}".format(sign,\
                                    str(numerator//\
                                    gcd(numerator,denominator))\
                                       .replace("-","")
                                    ,str(denominator\
                                       //gcd(numerator,denominator))\
                                       .replace("-",""))
main()
