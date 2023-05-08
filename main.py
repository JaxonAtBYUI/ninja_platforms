import pygame
import levels

"""
MAIN

This is the location of the main game loop. It houses the main varaibles used
for initializing a pygame window, and creates an instance of a room within the
game to hold all of the objects required to run the game. The step and draw
events are held within this loop.

Variables:
 - WIDTH, HEIGHT: The width and height of the pygame window.
 - WIN: The pygame window object
 - CLOCK: A pygame clock used for controlling FPS
 - FPS: The defined frames per second the game will run in.

Methods:
 - main: As described above, runs the main game loop
 - process_event: A function that handles checking pygame events.
"""

# Constants
WIDTH, HEIGHT = 800, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()
FPS = 30

pygame.init()
pygame.display.set_caption("Ninja Platforms")


def main():

    roomObject = levels.Level1()

    # Game Loop
    while True:
        CLOCK.tick(FPS)

        # Checks for exit of game
        if process_events() == False: break

        roomObject.step()
        roomObject.draw()

        # Refresh the screen.
        pygame.display.update()
        
    # Exit the program if we have exited the game loop
    pygame.quit()


def process_events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False            

    return True

if __name__ == "__main__":
    main()