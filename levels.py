import pygame
import room
import player
import camera
import solid

class Level1(room.Room):

    def __init__(self):
        super().__init__()
        self.generate_room("assets/level1.png")
        self.gravity = 2

    def draw(self):
        self.cam.update_position((self.player.rect.center))
        super().draw()