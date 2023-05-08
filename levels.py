import pygame
import room
import player
import camera
import solid

"""
LEVELS

A temporary way to store any levels that are made in the game.
Each level is an instance room that has had it's variables overwritten.
In the future this would be scrapped for a more easily expanded format
such as saving all the data for each level in a JSON file.
"""


class Level1(room.Room):

    def __init__(self):
        super().__init__()
        self.generate_room("assets/level1.png")
        self.gravity = 2

    def draw(self):
        self.cam.update_position((self.player.rect.center))
        super().draw()