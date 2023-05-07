import pygame
import physicsObject

class Player(physicsObject.PhysicsObject):

    def __init__(self, x, y, w, h, image="assets/ninja.png"):
        super().__init__(x, y, w, h, image)
        self.max_jumps = 2
        self.jumps = 2

    def create(self):
        pass

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
                

            


    
