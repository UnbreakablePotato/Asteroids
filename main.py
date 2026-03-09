import pygame
import constants
from logger import log_state
from logger import log_event
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

pygame.init()
clock = pygame.time.Clock()




def gameloop():
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    ast = AsteroidField()
    p1 = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) 
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")

        for p in drawable:
            p.draw(screen)
            for asteroid in asteroids:
                if asteroid.collides_with(p1):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
        
        pygame.display.flip()
        dt = clock.tick(60)/1000


        
        


if __name__ == "__main__":
    gameloop()