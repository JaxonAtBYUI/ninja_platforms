import pygame

"""
OBJECT

The basic template for any object that will appear in ROOM. It holds the basic
layout for position, as well as contains each event that can be called by room.
Allows for the checking of when a key is initially pressed or released as to
allow certain objects to be interactable.

Attributes:
 - rect: A pygame rect, which keeps track of the position and dimensions of an object.
 - image: A pygame image, which loads an image file to be displayed to the screen.
 - room: The instance of the ROOM this object is contained in.

Methods:
 - step: An event that is meant to be called each frame.
 - draw: An event that is meant to be called each frame after the step event has occured.
 - create: An event that is meant to be called upon creations, similar to __init__
           however it is meant to run code that has effects on other objects.
 - destroy: Code run when the object is "destroyed", however that is defined for that object.
 - key_pressed: Checks when a key is initially pressed.
 - key_released: Checks when a key is released.
 - collided_with: Code run when an object has a special event tied to a collision.

"""

class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, image="assets/error.png"):
        # self.room is set by room.py
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(image).convert()
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