import pygame
import object

"""
SOLID

A special type of object. It is a generic solid which physics objects will not pass through.

Attributes and methods inhereted from OBJECT

"""

class Solid(object.Object):

    def __init__(self, x, y, w, h, image="assets/wall.png"):
        super().__init__(x, y, w, h, image)
        