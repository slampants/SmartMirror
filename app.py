from time import sleep
from Visuals.constants import *
from Visuals.display import Display
from Visuals.stack import Stack
from Visuals.surface_generator import SurfaceGenerator
from Weather.weather_interface import WeatherManager

import pygame
import sys

WEATHERMAN = WeatherManager()
MAIN_STACK = Stack()
ContentManager = SurfaceGenerator()
DisplayManager = Display(k_SCREEN_WIDTH, k_SCREEN_HEIGHT)

pygame.init()

if __name__ == "__main__":
    while True:
        try:
            print("Generating weather content")
            weather_content = WEATHERMAN.get_weather_content()
            MAIN_STACK.add_to_stack(weather_content)
            DisplayManager.display_stack(MAIN_STACK)
            sleep(60)

        except KeyboardInterrupt:
            pygame.quit()
            sys.exit(0)
