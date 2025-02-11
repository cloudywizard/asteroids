import pygame

from constants import *

def main():
    pygame.init()

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    surface = pygame.display.get_surface()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        pygame.Surface.fill(surface, (0,0,0))

        pygame.display.flip()

    # print("Starting asteroids!")
    # print(f"Screen width: 1280")
    # print(f"Screen height: 720")

if __name__ == "__main__":
    main()