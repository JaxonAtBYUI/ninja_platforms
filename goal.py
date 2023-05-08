import pygame
import object
import player

"""
GOAL

A special type of OBJECT. Currently causes the game to close when the player comes
in contact with it. This would be changed to increment the level in the future.

Attributes:
 - Inhereted from OBJECT

Method:
 - collided_with: Causes the program to exit when the player collides with the goal.
"""

class Goal(object.Object):

    def collided_with(self, obj):
        if isinstance(obj, player.Player):
            pygame.quit()