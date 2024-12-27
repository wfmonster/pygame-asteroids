import pygame 
from constants import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # use screens fill method to to fill with black
        screen.fill("black")


        pygame.display.flip()

   


if __name__ == "__main__":
    main()