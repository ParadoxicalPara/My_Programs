from graphics import *
from math import sqrt
from time import sleep
class CButton:
    """The button in this sense is a circlular button. Creates a circular button
of radius "radius" and label "label" whose center is at "center" on window
"win\""""
    def __init__(self, center, radius, label, win):
        self.win = win
        self.btn = Circle(center, radius)
        self.btn.setFill("lightgray")
        self.btn.setWidth(3)
        self.label = Text(center, label)
        self.label.setSize(8)
        self.btn.draw(self.win)
        self.label.draw(self.win)
        self.deactivate()
        self.active = False
        self.anime = True
    def getLabel(self):
        """Returns the label of the circular button"""
        return self.label.getText()
    def activate(self):
        """Makes button active in the window"""
        self.btn.setWidth(3)
        self.label.setFill("black")
        self.anime = True
        self.active = True
    def deactivate(self):
        """Makes button inactive in the window"""
        self.btn.setWidth(1)
        self.label.setFill("grey")
        self.anime = False
        self.active = False
    def animate(self):
        """Animates when the button is clicked"""
        if self.anime:
            self.deactivate()
            sleep(0.2)
            self.activate()
    def clicked(self, click):
        """Checks if button has been clicked by getting click"""
        x1, y1 = click.getX(), click.getY()
        x2, y2 = self.btn.getCenter().getX(), self.btn.getCenter().getY()
        return sqrt((x2-x1)**2 + (y2-y1)**2)<= self.btn.getRadius() and \
               self.active

            
class button:
    """A button is a labeled rectangle in a window.
It is activated or deactivated with the activate()
and deactivate() methods. The clicked(p) method
returns true if the button is active and pis inside"""
    def __init__(self, center, width, height, label, win):
        """Creates a button having a label 'label' with width 'width' and
height 'height' at a location 'center' on a window "win"."""
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmax, self.ymax = x+w, y+h
        self.xmin, self.ymin = x-w, y-h
        self.frame = Rectangle(Point(self.xmax,self.ymax),\
                               Point(self.xmin, self.ymin))
        self.frame.setWidth(3)
        self.frame.setFill("lightgray")
        self.label = Text(center, label)
        self.label.setSize(8)
        self.frame.draw(win)
        self.label.draw(win)
        self.deactivate()
        self.active = False
        self.anime = False
    def animate(self):
        """Animates when the button is clicked"""
        if self.anime:
            self.deactivate()
            sleep(0.2)
            self.activate()
    def getLabel(self):
        """ Returns the label of the button"""
        return self.label.getText()
    def activate(self):
        """Makes button active in the window"""
        self.label.setFill("black")
        self.frame.setWidth(3)
        self.anime = True
        self.active = True
    def deactivate(self):
        """Makes button inactive in the window"""
        self.label.setFill("grey")
        self.frame.setWidth(1)
        self.anime = False
        self.active = False
    def clicked(self, click):
        """Checks whether a button has been clicked (i.e whether point 'p'
is in button) by returning True or False"""
        return (self.active and self.xmin<=click.getX()<=self.xmax and \
                self.ymin<=click.getY()<=self.ymax)
