import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y) , self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()# deletes the asteroid
        if self.radius <= ASTEROID_MIN_RADIUS: # if the radius of the asteroid is less or equal to the min  do nothing
            return ("this was a small asteroid and we're done")
        random_angle = random.uniform(20, 50) # create a random angle
        rotated1 = self.velocity.rotate(random_angle) # create a rotated velocity
        rotated2 = self.velocity.rotate(-random_angle) # the same but in the opposite direction
        new_radius = self.radius - ASTEROID_MIN_RADIUS # create a new radius about half the size
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) # create new asteroids with the new radius
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = rotated1 * 1.2 # assign velocity to the new asteroids
        asteroid2.velocity = rotated2 * 1.2



        