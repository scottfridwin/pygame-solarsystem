# constants.py
"""
constants.py - A module containing constants to be used by other files.

"""


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
