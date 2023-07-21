"""projectile.py provides a simple class for modelling the motion of \
a projecile"""
from math import sin, cos, radians
class projectile:
    """Simulates the flight of a projectile (under no air or wind resistance)
. It models via the horizontal and vertical components of the projectile"""
    def __init__(self, velocity, angle, height):
        """Create a projectile with given initial velocity, \
launch angle and initial height"""
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.xpos = 0.0
        self.ypos = height
    def getY(self):
        """Returns the latest height of the projectile"""
        return self.ypos
    def getX(self):
        """Returns the latest horizontal distance travelled by the \
projecitle"""
        return self.xpos
    def update(self, time):
        """This updates the position and velocity of the projectile \
at a given time"""
        self.xpos = self.xpos + self.xvel*time
        yvel1 = self.yvel + 9.8*time
        self.ypos = self.ypos - time*(self.yvel + yvel1)/2.0
        self.yvel = yvel1
