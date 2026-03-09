import pygame
import constants
from logger import log_state
import player

pygame.init()
clock = pygame.time.Clock()
dt = 0



def gameloop():
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable,drawable)
    p1 = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for p in drawable:
            p.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        for p in updatable:
            p.update(dt)
        
        


if __name__ == "__main__":
    gameloop()