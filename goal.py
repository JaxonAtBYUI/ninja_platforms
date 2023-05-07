import pygame
import object
import player

class Goal(object.Object):

    def collided_with(self, obj):
        if isinstance(obj, player.Player):
            print("Yay!")
            pygame.quit()