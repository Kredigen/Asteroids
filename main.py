# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers =(updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots ,updatable, drawable)
    # This line INSTANTIATES the Player class
    # It creates an actual Player object and stores it in the variable 'player'
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        global PLAYER_LIFE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") 
        updatable.update(dt)
        for aste in asteroids:
            if aste.check_collision(player):
                if PLAYER_LIFE > 0:
                    PLAYER_LIFE -= 1
                    print(PLAYER_LIFE)
                elif PLAYER_LIFE == 0 :
                    sys.exit("Game over!")
        for aste in asteroids:
            for shot in shots:
                #print(f"Checking collision between asteroid at {aste.position} and shot at {shot.position}")
                if aste.check_collision(shot):
                    #print("Collision detected!")
                    shot.kill()
                    aste.split()
        for draws in drawable:
            draws.draw(screen)
        updatable.update(dt)
        dt = clock.tick(60)/1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
