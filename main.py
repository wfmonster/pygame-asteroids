import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()   

    p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    astroidField = AsteroidField()

    # adds the player object to the both the updatable and drawable groups.
    updatable.add(p)
    updatable.add(astroidField)
    drawable.add(p)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
 
  
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # use screens fill method to to fill with black
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        for obj in updatable:
            obj.update(dt)
        
        for a in asteroids:
            if a.detect_collision(p):
                print("Game Over")
                exit(0)

        for a in asteroids:
            for b in shots:
                if a.detect_collision(b):
                    a.split() 

        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000 # converts to milliseconds
   


if __name__ == "__main__":
    main()