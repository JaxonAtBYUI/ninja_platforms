import pygame
import object

"""
DEATH

A special type of OBJECT. Causes whatever comes into contact with it to be destroyed.

Attributes:
 - Inhereted from OBJECT

Method:
 - collided_with: Runs the destroy function on any object it comes into contact with.
"""

class Death(object.Object):

    def collided_with(self, obj):
        obj.destroy()