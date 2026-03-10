import circleshape
from constants import *

import pygame
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cd = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white", self.triangle(),LINE_WIDTH)

    
    def rotate(self,dt):
        self.rotation += dt*PLAYER_TURN_SPEED


    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        speed_vector = rotated_vector*PLAYER_SPEED * dt
        self.position += speed_vector

    def update(self, dt):
        self.shot_cd -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cd > 0:
                do_nothing = 0
            else:
                self.shoot()
                self.shot_cd = PLAYER_SHOOT_CD

    def shoot(self):
        bullet = Shot(self.position.x,self.position.y,SHOT_RADIUS)
        #bullet = pygame.Vector2(0,1)
        rotated_bullet = pygame.Vector2(0,1).rotate(self.rotation)
        bullet.velocity = rotated_bullet*PLAYER_SHOOT_SPEED
        

        