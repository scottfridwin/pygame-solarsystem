# body.py
"""
body.py - A module containing information related to rendering and manging an object in space.

This module defines one class:
- Body: Represents a body in an orbital simulation.
"""

import math
from constants import Colors, Physics
import pygame


class Body:

    def __init__(self, x: float, y: float, vel_x: float, vel_y: float, m: float, r: float, color: tuple[int, int, int]):
        """
        Initialize a 'Body' object with necessary starting values.

        Args:
            x (float): The body's starting location on the x-axis.
            y (float): The body's starting location on the y-axis.
            vel_x (float): The body's starting velocity on the x-axis.
            vel_y (float): The body's starting velocity on the y-axis.
            m (float): The body's mass in kg.
            r (float): The body's radius in pixels (only used to draw the body).
            color (float): The body's color (only used to draw the body).
        """
        self.x = x          # initial x location
        self.y = y          # initial y location
        self.vel_x = vel_x  # initial x velocity
        self.vel_y = vel_y  # initial y velocity
        self.m = m          # mass
        self.r = r          # draw radius
        self.color = color  # draw color

    def draw(self, scale: float, win: pygame.Surface):
        """
        Draw the body in the simulation window.

        Args:
            scale (float): The scale of the simulation window.
            win (pygame.Surface): The window in which to draw the body.
        """

        # Calculates the center point of the object
        x = self.x * scale + win.get_width() / 2
        y = self.y * scale + win.get_height() / 2

        # Draws a circle with radius r centered on the point (x, y)
        pygame.draw.circle(win, self.color, (x, y), self.r)

    def calculate_gravity(self, other: 'Body') -> tuple[float, float]:
        """
        Calculate the gravitational force between this body and another body.

        Args:
            other (Body): Another Body instance.

        Returns:
            tuple[float, float]: The gravitational force components (force_x, force_y).
        """
        # Calulate the distance between the bodies
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        # Calculate the gravitational force
        force = Physics.G * self.m * other.m / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, all_bodies: list['Body'], timestep: float) -> None:
        """
        Update the position and velocity of the body based on gravitational forces.

        Args:
            all_bodies (list[Body]): List of all bodies in the system.
            timestep (float): Time interval for the update in seconds.
        """
        total_fx = total_fy = 0  # Start from initial values of no total force

        # For each body in the system, calculate the gravitational force
        for body in all_bodies:
            if self == body:
                continue

            fx, fy = self.calculate_gravity(body)

            # Add the force to the total
            total_fx += fx
            total_fy += fy

        # Update the current velocity
        self.vel_x += total_fx / self.m * timestep
        self.vel_y += total_fy / self.m * timestep

        # Update the current location
        self.x += self.vel_x * timestep
        self.y += self.vel_y * timestep
