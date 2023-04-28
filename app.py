from time import sleep
from Visuals.constants import *
from Visuals.display import Display
from Visuals.stack import Stack
from Weather.weather_interface import WeatherManager

import pygame

WEATHERMAN = WeatherManager()
MAIN_STACK = Stack()
DisplayManager = Display(k_SCREEN_WIDTH, k_SCREEN_HEIGHT)

pygame.init()
pygame.mouse.set_visible(False)

if __name__ == "__main__":
    while True:
        weather_content = WEATHERMAN.get_weather_content()
        MAIN_STACK.add_to_stack(weather_content)
        DisplayManager.display_stack(MAIN_STACK)
        sleep(60)
