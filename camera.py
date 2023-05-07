import pygame

class Camera():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()

    def update_position(self, point):
        # Center the camera on the player's position
        self.x = point[0] - round(self.width / 2.0)
        self.y = point[1] - round(self.height / 2.0)

    def draw_object(self, image, point):
        x_offset = point[0] - self.x
        y_offset = point[1] - self.y
        self.screen.blit(image, (x_offset, y_offset))

    # Draws a background with paralax
    def draw_background(self, image, size):
        width, height = image.get_size()
        
        per_x = self.x / size[0]
        per_y = self.y / size[1]

        x_offset = (per_x * (width * .2)) + 32
        y_offset = per_y * (height * .2) + 32

        self.screen.blit(image, (-x_offset, -y_offset))

    