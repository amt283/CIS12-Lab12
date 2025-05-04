from planet import Planet
from solar_system import SolarSystem
import turtle
from sun import Sun

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.__solar_system = SolarSystem()
        self.__width = width
        self.__height = height
        self.__num_periods = num_periods
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width=self.__width, height=self.__height)
        self.__screen.bgcolor("black")
        self.__t.clear()

    def run(self):
        self.__solar_system.show_planets()
        for a_move in range(self.__num_periods):
            self.__solar_system.move_planets()
            self.__solar_system.show_planets()
        self.freeze()

    def freeze(self):
        self.__screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800,0,0)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 100, 25, 5.0, 200.0, -15, 40,"green")
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, 50, 62, 10.0, 125.0, -15, 40,"red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()
