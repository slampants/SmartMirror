import sys

from time import sleep
from Visuals.surface_generator import SurfaceGenerator
from Visuals.stack import Stack
from Weather.weather_interface import WeatherInterface
import pygame

# CONSTANTS
k_WIDTH = 500
k_HEIGHT = 600

# INITIALIZE
pygame.init()

WeatherManager = WeatherInterface()
StackManager = Stack()
SurfaceManager = SurfaceGenerator(k_WIDTH)

screen = pygame.display.set_mode((k_WIDTH, k_HEIGHT))

# BUILD STACK
StackManager.add_to_stack(SurfaceManager.text_surface("Current weather:"))
current_weather_icon = SurfaceManager.icon_surface(WeatherManager.current_weather.get_icon_filename())

StackManager.add_to_stack(current_weather_icon)
current_weather_description = WeatherManager.get_current_weather_description()

StackManager.add_to_stack(SurfaceManager.text_surface(current_weather_description))
precip_string = WeatherManager.get_next_precipitation_string()

StackManager.add_to_stack(SurfaceManager.text_surface(precip_string))
# StackManager.add_to_stack(SurfaceManager.image_surface("Friedman.Samuel.jpg"))
ultra_long_string = "Long " * 100
StackManager.add_to_stack(SurfaceManager.text_surface(ultra_long_string))

# BLIT
StackManager.draw_stack_to_screen(screen)
# FLIP
pygame.display.flip()

while True:
    try:
        print("Waiting...")
        sleep(1)
    except KeyboardInterrupt:
        pygame.quit()
        print("Bye!")
        sys.exit(0)

# TODO: Use the Display class to actually generate all your content, adding a timer, etc, inside while loop
