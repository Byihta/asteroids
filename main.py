import pygame
from constants import *

def main():
    print("Starting Asteroids!")

if __name__ == '__main__':
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True
    dt = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill('black')
        pygame.display.flip()
        dt += clock.tick(60) / 1000

