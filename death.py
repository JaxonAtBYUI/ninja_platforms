import pygame
import object

class Death(object.Object):

    def collided_with(self, obj):
        obj.destroy()