from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "small asteroid"
        log_event("asteroid_split")
        r = random.uniform(20,50)
        angle = self.velocity.rotate(r)
        neg_angle = self.velocity.rotate(-r)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x,self.position.y,new_radius)
        ast2 = Asteroid(self.position.x,self.position.y,new_radius)
        ast1.velocity = angle * 1.2
        ast2.velocity = neg_angle * 1.2

