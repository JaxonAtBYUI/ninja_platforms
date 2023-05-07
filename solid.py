import pygame
import object

class Solid(object.Object):

    def __init__(self, x, y, w, h, image="assets/wall.png"):
        super().__init__(x, y, w, h, image)
        