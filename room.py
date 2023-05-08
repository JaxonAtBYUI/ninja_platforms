import pygame
import camera
import json
import solid
import player
import death
import goal

"""
ROOM

An object which contains the enviornment of the game. It keeps track of and runs
all objects within it. 

Attributes:
 - gravity: The strength of gravity in the room. Used by physics objects.
 - objects: An array of all objects within the room.
 - spawn_point: Player object specific. Records the start position of the player.
 - drag: The 'air friction' within the room. Controls how quickly objects slow down.
 - friction: The standard amount of 'friction' between physics objects within the room.
 - screen: The pygame display surface.
 - background: The background image of the room.
 - cam: The camera that the room calls to draw all objects.

Methods:
 - create_object: Takes an object and adds it to the object array, therby creating it within the room.
 - destroy_objects: Takes a specific object in the room, and removes it from the object array.
 - step: Gets the inputs from the user and runs the step event for all objects in the room.
 - draw: Fills the room background with a color then calls the camera to draw the background and objects.
 - generate_room: Creates all the objects in a room based on an image file that has been loaded.

"""


class Room():
    
    def __init__(self):
        self.gravity = 10
        self.objects = []
        self.spawn_point = (0, 0)
        self.drag = .93
        self.friction = .2
        self.screen = pygame.display.get_surface()
        self.background = pygame.image.load("assets/background.png").convert()
        self.cam = camera.Camera()
    
    def create_object(self, obj):
        self.objects.append(obj)
        obj.room = self

    def destroy_objects(self, obj):
        if obj in self.objects: self.objects.remove(obj)

    def step(self):
        self.keys = pygame.key.get_pressed()
        
        for obj in self.objects:
            obj.step()
        
        self.keys_last = self.keys

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.cam.draw_background(self.background, self.size)
        for obj in self.objects:
            obj.draw()

    def generate_room(self, image_file):
        # Get dictionary of objects as related to their colors
        with open('objects.json', 'r') as f:
            object_textures = json.load(f)

        image = pygame.image.load(image_file)
        width, height = image.get_size()
        self.size = (32 * width, 32 * height)

        for x in range(width):
            for y in range(height):

                color = image.get_at((x, y))
                
                # Adds a solid at each place a solid is to be added
                if object_textures[str(color)] != False:
                    obj = solid.Solid(x * 32, y * 32, 32, 32, object_textures[str(color)])
                    self.create_object(obj)
                
                # Create the death blocks
                if color == (255, 0, 0, 255):
                    obj = death.Death(x * 32, y * 32, 32, 32, "assets/death.png")
                    self.create_object(obj)

                # Create the death blocks
                if color == (255, 255, 0, 255) : 
                    obj = goal.Goal(x * 32, y * 32, 32, 32,"assets/goal.png")
                    self.create_object(obj)

                # Sets spawn for player
                if color == (255, 0, 255, 255):
                    self.spawn_point = (x * 32, y * 32,)
                    self.player = player.Player(x * 32, y * 32, 32, 64)
                    self.create_object(self.player)
                

                
    


            
