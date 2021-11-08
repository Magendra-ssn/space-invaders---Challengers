import pygame
import colors
from  helpers import *

class Ship :
    def __init__(self, display, x, y) :
        self.x = x
        self.y = y
        self.width = 24
        self.height = 32
        self.color = colors.green
        self.rotation = 0
        self.points = [
            #A TOP POINT
            (self.x, self.y - (self.height / 2)),
            #B BOTTOM LEFT POINT
            (self.x - (self.width / 2), self.y + (self.height /2)),
            #C CENTER POINT
            (self.x, self.y + (self.height / 4)),
            #D BOTTOM RIGHT POINT
            (self.x + (self.width / 2), self.y + (self.height / 2)),
            #A TOP AGAIN
            (self.x, self.y - (self.height / 2)),
            #C A NICE LINE IN THE MIDDLE
            (self.x, self.y + (self.height / 4)),
        ]

    def move(self, strdir) :
        dir = 0
        if strdir == 'left' :
            dir = -3
        elif strdir == 'right' :
            dir = 3

        self.points = rotate_polygon((self.x, self.y), self.points, dir)
def draw(self, display):
        stroke = 2
        pygame.draw.lines(display, self.color, False, self.points, stroke)