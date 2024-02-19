# body.py
"""
body.py - A module containing information related to rendering and manging an object in space.

This module defines one class:
- Body: Represents a body in an orbital simulation.
"""

import math
from constants import Colors
import pygame


class Body:

    def __init__(self, x: float, y: float):
        """
        Initialize a 'Body' object with necessary starting values.

        Args:
            x (float): The body's starting location on the x-axis.
            y (float): The body's starting location on the y-axis.


        TODO: Update this method to set starting velocity, mass, size, and color
        """
        self.x = x
        self.y = y

    def draw(self, scale: float, win: pygame.Surface):
        """
        Draw the body in the simulation window.

        Args:
            scale (float): The scale of the simulation window.
            win (pygame.Surface): The window in which to draw the body.

        TODO: Update this method to draw a different color and size of circle
        """

        # Calculates the center point of the object
        x = self.x * scale + win.get_width() / 2
        y = self.y * scale + win.get_height() / 2

        # Draws a white circle with radius 10 centered on the point (x, y)
        pygame.draw.circle(win, Colors.White, (x, y), 10)

    def calculate_gravity(self, other: 'Body') -> tuple[float, float]:
        """
        Calculate the gravitational force between this body and another body.

        Args:
            other (Body): Another Body instance.

        Returns:
            tuple[float, float]: The gravitational force components (force_x, force_y).
        """
        # TODO: Calculate the gravitational force based on the body masses and distance
        force_x = 0
        force_y = 0

        return force_x, force_y

    def update_position(self, all_bodies: list['Body'], timestep: float) -> None:
        """
        Update the position and velocity of the body based on gravitational forces.

        Args:
            all_bodies (list[Body]): List of all bodies in the system.
            timestep (float): Time interval for the update in seconds.
        """
        total_fx = total_fy = 0  # Start from initial values of no total force

        # TODO: Update the current velocity and location of this body based on the total gravitational force
