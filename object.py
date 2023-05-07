import pygame

class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, image="assets/error.png"):
        # self.room is set by room.py
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(image)
        self.create()

    def step(self):
        pass        

    def draw(self):
        if self.image != None: self.room.cam.draw_object(self.image, self.rect.topleft)

    def create(self):
        pass

    def destroy(self):
        self.room.remove(self)
        self._destroy()

    def key_pressed(self, key_code):
        if self.room.keys[key_code] and not self.room.keys_last[key_code]:
            return True
        return False

    def key_released(self, key_code):
        if not self.room.keys[key_code] and self.room.keys_last[key_code]:
            return True
        return False
    
    def collided_with(self, obj):
        pass