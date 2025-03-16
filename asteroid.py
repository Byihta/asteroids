import pygame
from circleshape import CircleShape
from constants import *
from random import uniform
from collections import namedtuple

Random = namedtuple('random', ['uniform'])
random = Random(uniform)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.color.Color(255,255,255), self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            deflectionAngle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_pos = Asteroid(*self.position, new_radius)
            asteroid_neg = Asteroid(*self.position, new_radius)
            asteroid_pos.velocity = self.velocity.rotate(deflectionAngle)
            asteroid_neg.velocity = self.velocity.rotate(-deflectionAngle)

        

            