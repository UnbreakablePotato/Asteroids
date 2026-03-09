import circleshape
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
import pygame

class Player(circleshape.CircleShape):
    def __init(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon("white", self.triangle(),LINE_WIDTH)