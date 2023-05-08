import pygame
import object

"""
PHYSICS OBJECT

A special type of object. This object obeys the rules of physics as defined in the room,
and being able to move. Inherets from the OBJECT class.

Attributes:
 - x_velocity: The velocity in the x direction
 - y_velocity: The velocity in the y direction

Methods:
 - step: Handles the movement of the object. This means handling the change in position as well as
         handling collision events.
 - apply_force: Applies a force to the object via adding to the velocity of the object in a given direction
 - apply_multiplier: Applies a multiplier to the player's velocity. Use described below.
 - check_collision: Checks to see if the object is currently colliding with any other object.
 - increment: Handles collision with solid objects via incrementally moving to where the two objects meet.

"""


class PhysicsObject(object.Object):

    def __init__(self, x, y, w, h, image):
        super().__init__(x, y, w, h, image)
        # Physics variables
        self.x_velocity = 0.0
        self.y_velocity = 0.0

    def step(self):
        
        # Test for movement. If velocity is under a certain threshold, set the velocity to 0
        if abs(self.x_velocity) < .1 and self.x_velocity:
            self.apply_multiplier((0, 1))
        if abs(self.y_velocity) < .1 and self.y_velocity:
            self.apply_multiplier((1, 0))
        
        # Move the object in the x direction
        self.rect.move_ip(self.x_velocity, 0)
        collisions = self.check_collision()
        if collisions != []:
            for obj in collisions:
                obj.collided_with(self)
            self.rect.move_ip(self.x_velocity * -1, 0)
            self.increment(self.x_velocity, 0)
            self.x_velocity = 0

        # Move the object in the y direction
        self.rect.move_ip(0, self.y_velocity)
        collisions = self.check_collision()
        if collisions != []:
            for obj in collisions:
                obj.collided_with(self)
            self.rect.move_ip(0, self.y_velocity * -1)
            self.increment(0, self.y_velocity)
            self.y_velocity = 0
    
    def apply_force(self, force=(0.0, 0.0)):
        self.x_velocity += force[0]
        self.y_velocity += force[1]
    
    """
    Apply Multiplier

    This accounts for inertia and resistance by multiplying
    the speed by a given number each frame. This also limits
    the max speed of an object. 1.0 means that 100% speed is
    maintained, whereas 0.5 would mean that only 50% speed is
    maintained. This means that an object takes longer to
    accelerate.

    Limiting is based on the multiplier's ratio to the 'forces'
    induced on the object. Example: The player has 1 added to
    their overall x velocity each frame the 'd' key is held. If
    the multiplier is .9, then the speed will never exceed 9.
    """

    def apply_multiplier(self, multiplier=(1.0, 1.0)):
        self.x_velocity *= multiplier[0]
        self.y_velocity *= multiplier[1]

    def check_collision(self):
        collisions = []

        for object in self.room.objects:
            if object is not self:
                if self.rect.colliderect(object.rect):
                    collisions.append(object)
        
        return collisions

    def increment(self, translation_x, translation_y):
        # Get the starting position
        x = self.rect.x
        y = self.rect.y

        # Get the direction being traveled in.
        if translation_x: tx_sign = translation_x / abs(translation_x)
        if translation_y: ty_sign = translation_y / abs(translation_y)

        # Get the end point
        end_x = x + translation_x
        end_y = y + translation_y

        # While not touching the other object
        x_complete = False
        y_complete = False
        while not x_complete and not y_complete:

            # Increment in the x direction until one of the following is met:
            #   1. You have reached the end point in the x direction without a collision.
            #   2. You have collided with an object on your way to the endpoint.
            if translation_x and not x_complete:
                self.rect.move_ip(1 * tx_sign, 0)

                if self.check_collision() != []:
                    # Back out of object and report that you have collided.
                    self.rect.move_ip(-1 * tx_sign, 0)
                    x_complete = True
                elif self.rect.x == end_x:
                    x_complete = True

            # The same loop for the x direction but in the y direction.
            if translation_y and not y_complete:
                self.rect.move_ip(0, 1 * ty_sign)

                if self.check_collision() != []:
                    self.rect.move_ip(0, -1 * ty_sign)
                    y_complete = True
                elif self.rect.y == end_y:
                    y_complete = True