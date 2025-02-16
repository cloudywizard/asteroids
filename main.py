import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    screen = pygame.display.get_surface()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")

                sys.exit()

            for shot in shots:
                if asteroid.is_collision(shot):
                    asteroid.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    # print("Starting asteroids!")
    # print(f"Screen width: 1280")
    # print(f"Screen height: 720")

if __name__ == "__main__":
    main()