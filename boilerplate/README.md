# Boilerplate 

This directory contains the lowest amount of completed code in this lesson. There is some basic boilerplate code and pseudo-code comments that indicate the changes that need to be made.

# Implementation examples

This section indicates the different "TODO" comments in the boilerplate code and an example of how they can be implemented.

## constants.py
<details>
  <summary><i>TODO: Define additional colors that can be used for our simulation</i></summary>

  ```
class Colors:
    """
    A custom class for representing color constants.

    Use these color constants to enhance readability and maintainability
    in your code. Each color is represented as an RGB tuple.
    """
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    DARK_GREY = (80, 78, 81)
  ```

</details>
<details>
  <summary><i>TODO: Define another class that contains know constants for scientific calculations</i></summary>

  ```
class Physics:
    """
    A class containing physical constants used in scientific calculations.
    """

    """
    Astronomical Unit (AU) in meters

    Represents the astronomical unit (AU), which is the average distance
      between the Earth and the Sun. It is expressed in meters (149.6 million kilometers).
    """
    AU = 149.6e6 * 1000

    """
    Gravitational constant (G) in m³ kg⁻¹ s⁻²

    Represents the gravitational constant (G), which determines the strength
      of gravitational interactions between masses. It has a value of approximately
      6.67428 × 10⁻¹¹ m³ kg⁻¹ s⁻².
    """
    G = 6.67428e-11
  ```

</details>

## body.py

<details>
  <summary><i>TODO: Update this method to set starting velocity, mass, size, and color</i></summary>

  ```
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
  ```

</details>
<details>
  <summary><i>TODO: Update this method to draw a different color and size of circle</i></summary>

  ```
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
  ```

</details>
<details>
  <summary><i>TODO: Calculate the gravitational force based on the body masses and distance</i></summary>

  ```
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
  ```

</details>
<details>
  <summary><i>TODO: Update the current velocity and location of this body based on the total gravitational force</i></summary>

  ```
    def update_position(self, all_bodies: list['Body'], timestep: float) -> None:
        """
        Update the position and velocity of the body based on gravitational forces.

        Args:
            all_bodies (list[Body]): List of all bodies in the system.
            timestep (float): Time interval for the update in seconds.
        """
        total_fx = total_fy = 0 # Start from initial values of no total force

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
  ```

</details>

## main.py

<details>
  <summary><i>TODO: Add bodies to be simulated</i></summary>

  ```
    # Add bodies to be simulated
    sun = Body(0, 0, 0, 0, 1.98892 * 10**30, 30, Colors.YELLOW)
    bodies.append(sun)

    earth = Body(-1 * Physics.AU, 0, 0, 29.783 * 1000,
                 5.9742 * 10**24, 16, Colors.BLUE)
    bodies.append(earth)
  ```

</details>
<details>
  <summary><i>TODO: Update the position of each body and draw it in the window</i></summary>

  ```
  for body in bodies:
      body.update_position(bodies, timestep)
      body.draw(scale, window)
  ```

</details>