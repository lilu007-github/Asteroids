# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers =  updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    dt = 0
    #pygame.display.set_caption("Asteroids")

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)  # Update all updatable sprites

        for asteroid in asteroids:
            if asteroid.collide_with(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collide_with(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))  # Fill the screen with black

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000  # Cap the frame rate at 60 FPS
        
    
    #pygame.quit()

if __name__ == "__main__":
    main()
