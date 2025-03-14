import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color=(255,255,255), center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            piece1 = Asteroid(self.position.x, self.position.y, new_radius)
            piece2 = Asteroid(self.position.x, self.position.y, new_radius)

            piece1.velocity = self.velocity.rotate(random.uniform(20,50)) * 1.2
            piece2.velocity = self.velocity.rotate(-random.uniform(20,50)) * 1.2