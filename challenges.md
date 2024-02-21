# Challenges 

Once you have a good grasp of how the simulation works, here are some challenges that you can try.

## Complete our solar system

This challenge is pretty straightforward: Add the rest of the planets in our solar system. You will have to adjust the scale of the simulation to be able to see all of the planets.

<details>
  <summary><i>Expand for solution</i></summary>

  First, we will need to add some new colors in the Colors class:

  ```diff
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    DARK_GREY = (80, 78, 81)
  + GREY_BROWN = (128, 128, 128)
  + YELLOW_WHITE = (255, 255, 224)
  + RUSTY_RED = (188, 39, 50)
  + ORANGE = (255, 165, 0)
  + PALE_YELLOW = (255, 255, 204)
  + PALE_BLUE_GREEN = (173, 216, 230)
  + DEEP_BLUE = (0, 0, 128)
  ```

  Then we can add the rest of the planets:

  ```diff
    sun = Body(0, 0, 0, 0, 1.9891e30, 20, Colors.YELLOW)
    bodies.append(sun)

  + mercury = Body(5.79e10, 0, 0, -47.87e3,
  +                3.30e23, 7.5, Colors.GREY_BROWN)
  + bodies.append(mercury)
  +
  + venus = Body(1.082e11, 0, 0, 35.02e3,
  +              4.87e24, 8.5, Colors.YELLOW_WHITE)
  + bodies.append(venus)
  +
    earth = Body(Physics.AU, 0, 0, -29.783e3,
                 5.97e24, 9, Colors.PURE_BLUE)
    bodies.append(earth)

  + mars = Body(2.28e11, 0, 0, -24.077e3,
  +             6.42e23, 8.75, Colors.RUSTY_RED)
  + bodies.append(mars)
  +
  + jupiter = Body(7.785e11, 0, 0, -13.07e3,
  +                1.898e27, 12, Colors.ORANGE)
  + bodies.append(jupiter)
  +
  + saturn = Body(1.432e12, 0, 0, -9.69e3,
  +               5.68e26, 10, Colors.PALE_YELLOW)
  + bodies.append(saturn)
  +
  + uranus = Body(2.867e12, 0, 0, 6.81e3,
  +               8.68e25, 9, Colors.PALE_BLUE_GREEN)
  + bodies.append(uranus)
  +
  + neptune = Body(4.515e12, 0, 0, -5.43e3,
  +                1.02e26, 9.75, Colors.DEEP_BLUE)
  + bodies.append(neptune)
  ```

  Lastly, we will adjust the scale of the simulation so we can see all the way out to Neptune:

  ```diff
  - scale = 250 / Physics.AU  # The scale for rendering objects in the simulation
  + scale = 20 / Physics.AU  # The scale for rendering objects in the simulation
  ```

</details>


## Add orbit lines

It's fun to see where a planet is, but what about seeing where it was? In this challenge you will add some additional code to the `draw` method to draw the body's orbital path in addition to its current location.

<details>
  <summary><i>Expand for solution</i></summary>

  In order to draw the orbital path, we need to keep track of where the body has been. This means adding a new variable to track the x and y position over time:

  This change adds a new field that will contain the history of our orbit.
  ```diff
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

  +     self.orbit = []
  ```

  and this change will track that history:
  ```diff
        # Update the current location
        self.x += self.vel_x * timestep
        self.y += self.vel_y * timestep

  +     self.orbit.append((self.x, self.y))
  ```

  After we have that orbital history in the `self.orbit` variable, we can add code to the `draw` method to draw the line:

  ```diff
          # Draws a circle with radius r centered on the point (x, y)
          pygame.draw.circle(win, self.color, (x, y), self.r)

  +       if len(self.orbit) > 2:
  +           scaled_points = []
  +           for x, y in self.orbit:
  +               scaled_points.append(
  +               (x * scale + win.get_width() / 2, y * scale + win.get_height() / 2))
  +           pygame.draw.lines(win, self.color, False, scaled_points, 2)
  ```

</details>


## Create a system with 2 stars

Can you create a solar system that contains 2 stars that orbit around each other in (mostly) stable orbits? 

<details>
  <summary><i>Expand for solution</i></summary>

  I don't have an actual solution here! This is the closest that I was able to get. I created 2 stars of equal mass and placed them at equal distance from the center point. It is almost stable, but they eventually get closer and closer until they crash!

```diff
-   sun = Body(0, 0, 0, 0, 1.9891e30, 20, Colors.YELLOW)
-   bodies.append(sun)
-
-   earth = Body(Physics.AU, 0, 0, 29.783e3,
-                5.97e24, 9, Colors.BLUE)
-   bodies.append(earth)
+   mass = 2e29
+   distance = Physics.AU
+   velocity = math.sqrt(Physics.G * mass * 2 / (distance * 2)) / 2
+   star1 = Body(distance, 0, 0, velocity, mass, 20, Colors.YELLOW)
+   bodies.append(star1)

+   star2 = Body(-1*distance, 0, 0, -1 * velocity, mass, 20, Colors.RED)
+   bodies.append(star2)
```


## Add a rogue planet/star to a stable system

_This challenge is best if you add it on top of the "Complete our solar system" and "Add orbit lines" challenges._

Can you add a rogue planet or star to a stable solar system and watch the resulting chaos?

<details>
  <summary><i>Expand for solution</i></summary>

  There are infinite possibilities for how you can do this. The example solution here shows adding a **massive** rogue star that plows through our solar system.

```diff
    uranus = Body(2.867e12, 0, 0, 6.81e3,
                  8.68e25, 9, Colors.PALE_BLUE_GREEN)
    bodies.append(uranus)

    neptune = Body(4.515e12, 0, 0, -5.43e3,
                   1.02e26, 9.75, Colors.DEEP_BLUE)
    bodies.append(neptune)

+   rogue = Body(10e13, 10.2e13, -2e5, -2e5, 5e32, 20, Colors.DARK_GREY)
+   bodies.append(rogue)
```
