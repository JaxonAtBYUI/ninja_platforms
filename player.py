import pygame
import physicsObject

"""
PLAYER

A special type of physics object. It is what the player controls on the screen.

Attributes:
 - max_jumps: The maximum times a player can jump before meeting the criteria to be able to jump again.
 - jumps: The remaining jumps the player has.

Methods:
 - step: Makes checks on the state of the player and the inputs, and applies forces accordingly.
 - destroy: When "destroyed" reset the player to the starting location of the ROOM.
 - user_inputs: Checks for specific inputs by the player, and applies forces accordingly.
 - replenish_jumps: Checks to see if the player meets the conditions for reseting their jumps.
 - wall_cling: Checks if the player is against a wall and is attempting to cling to it. If so, apply forces.
 - wall_jump: While the player is wall clinging, if they jump, push up and away from wall.

"""

class Player(physicsObject.PhysicsObject):

    def __init__(self, x, y, w, h, image="assets/ninja.png"):
        super().__init__(x, y, w, h, image)
        self.max_jumps = 2
        self.jumps = 2

    def step(self):
        
        self.replenish_jumps()
        self.user_inputs()
        self.apply_force((0, self.room.gravity))
        self.apply_multiplier((self.room.drag, 1))

        super().step()
    
    def destroy(self):
        self.rect.x, self.rect.y = self.room.spawn_point
        # self.x_velocity, self.y_velocity = 0.0, 0.0
        
    def user_inputs(self):
        if self.room.keys[pygame.K_d]:
            self.apply_force((1, 0))
            self.wall_cling()
        if self.room.keys[pygame.K_a]:
            self.apply_force((-1, 0))
            self.wall_cling()
        if self.key_pressed(pygame.K_w) or self.key_pressed(pygame.K_SPACE):
            if self.jumps > 0:
                self.apply_multiplier((1.0, 0.0))
                self.apply_force((0, self.room.gravity * -10))
                self.jumps -= 1

    def replenish_jumps(self):
        if self.jumps < self.max_jumps:
            self.rect.y += 1
            if self.check_collision() != []:
                self.jumps = self.max_jumps
            self.rect.y -= 1

    def wall_cling(self):
        if self.y_velocity > 0:
            
            if self.room.keys[pygame.K_d]:
                self.rect.x += 1
                if self.check_collision() != []:
                    self.apply_multiplier((1.0, self.room.friction))
                    self.wall_jump(-1)   
                self.rect.x -= 1


            if self.room.keys[pygame.K_a]:
                self.rect.x -= 1
                if self.check_collision() != []:
                    self.apply_multiplier((1.0, self.room.friction))
                    self.wall_jump(1)           
                self.rect.x += 1
    
    def wall_jump(self, direction):
        if self.key_pressed(pygame.K_w) or self.key_pressed(pygame.K_SPACE):
            self.apply_multiplier((1.0, 0.0))
            self.apply_force((10 * direction, self.room.gravity * -10))
            self.jumps = 1
                

            


    
