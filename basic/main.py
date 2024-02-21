import pygame
from constants import Colors, Physics
from body import Body
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
    # Add bodies to be simulated
    sun = Body(0, 0, 0, 0, 1.9891e30, 20, Colors.YELLOW)
    bodies.append(sun)

    earth = Body(Physics.AU, 0, 0, 29.783e3,
                 5.97e24, 9, Colors.BLUE)
    bodies.append(earth)

    run = True
    while run:
        clock.tick(60)

        # Fill the window with a black background
        window.fill((0, 0, 0))

        # Check if we are exiting the simulation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update the position of each body and draw it in the window
        for body in bodies:
            body.update_position(bodies, timestep)
            body.draw(scale, window)

        # Tell pygame to update the window
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
