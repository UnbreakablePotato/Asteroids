import pygame
import constants
from logger import log_state
import player

pygame.init()
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def gameloop():
    p1 = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        p1.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        p1.update(dt)
        
        


if __name__ == "__main__":
    gameloop()