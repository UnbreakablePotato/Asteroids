import pygame
import constants
from logger import log_state

pygame.init()
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def gameloop():
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    gameloop()