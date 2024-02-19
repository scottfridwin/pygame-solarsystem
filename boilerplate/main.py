import pygame
from body import Body
from constants import Physics
pygame.init()


def main():
    # Simulation preferences - Can be adjusted as desired
    timestep = 60*60*24*7  # 1 week in seconds
    window_width = 800
    window_height = 800
    scale = 250 / Physics.AU  # The scale for rendering objects in the simulation

    # pygame initialization
    window = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    bodies: list['Body'] = []
    # TODO: Add bodies to be simulated

    run = True
    while run:
        clock.tick(60)

        # Fill the window with a black background
        window.fill((0, 0, 0))

        # Check if we are exiting the simulation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # TODO: Update the position of each body and draw it in the window

        # Tell pygame to update the window
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
