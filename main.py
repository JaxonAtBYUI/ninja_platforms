import pygame
import levels

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