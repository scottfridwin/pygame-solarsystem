# Challenges 

Once you have a good grasp of how the simulation works, here are some challenges that you can try.

## Complete our solar system

This challenge is pretty straightforward: Add the rest of the planets in our solar system. You will have to adjust the scale of the simulation to be able to see all of the planets.

<details>
  <summary><i>Expand for solution</i></summary>

  First, we will need to add some new colors in the Colors class:

  ```
    GREY_BROWN = (128, 128, 128)
    YELLOW_WHITE = (255, 255, 224)
    RUSTY_RED = (188, 39, 50)
    ORANGE = (255, 165, 0)
    PALE_YELLOW = (255, 255, 204)
    PALE_BLUE_GREEN = (173, 216, 230)
    DEEP_BLUE = (0, 0, 128)
  ```

  Then we can add the rest of the planets:

  ```
    sun = Body(0, 0, 0, 0, 1.9891e30, 20, Colors.YELLOW)
    bodies.append(sun)

    mercury = Body(5.79e10, 0, 0, -47.87e3,
                   3.30e23, 7.5, Colors.GREY_BROWN)
    bodies.append(mercury)

    venus = Body(1.082e11, 0, 0, 35.02e3,
                 4.87e24, 8.5, Colors.YELLOW_WHITE)
    bodies.append(venus)

    earth = Body(Physics.AU, 0, 0, -29.783e3,
                 5.97e24, 9, Colors.PURE_BLUE)
    bodies.append(earth)

    mars = Body(2.28e11, 0, 0, -24.077e3,
                6.42e23, 8.75, Colors.RUSTY_RED)
    bodies.append(mars)

    jupiter = Body(7.785e11, 0, 0, -13.07e3,
                   1.898e27, 12, Colors.ORANGE)
    bodies.append(jupiter)

    saturn = Body(1.432e12, 0, 0, -9.69e3,
                  5.68e26, 10, Colors.PALE_YELLOW)
    bodies.append(saturn)

    uranus = Body(2.867e12, 0, 0, 6.81e3,
                  8.68e25, 9, Colors.PALE_BLUE_GREEN)
    bodies.append(uranus)

    neptune = Body(4.515e12, 0, 0, -5.43e3,
                   1.02e26, 9.75, Colors.DEEP_BLUE)
    bodies.append(neptune)
  ```

  Lastly, we will adjust the scale of the simulation so we can see all the way out to Neptune:

  ```
  scale = 20 / Physics.AU  # The scale for rendering objects in the simulation
  ```

</details>