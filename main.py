import pygame 
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # use screens fill method to to fill with black
        screen.fill("black")

        p.draw(screen)
        p.update(dt)
        
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000 # converts to milliseconds
   


if __name__ == "__main__":
    main()