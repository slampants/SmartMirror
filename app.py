from requests import ConnectionError
from time import sleep
from Visuals.constants import *
from Visuals.display import Display
from Visuals.error_content import ErrorContent
from Visuals.stack import Stack
from Weather.weather_interface import WeatherManager

import pygame

pygame.init()
pygame.mouse.set_visible(False)

WEATHERMAN = WeatherManager()
MAIN_STACK = Stack()
ERROR_CONTENT = ErrorContent.get_error_content()
DisplayManager = Display(k_SCREEN_WIDTH, k_SCREEN_HEIGHT)

if __name__ == "__main__":
    while True:
        try:
            weather_content = WEATHERMAN.get_weather_content()
            MAIN_STACK.add_to_stack(weather_content)
        except ConnectionError:
            MAIN_STACK.add_to_stack(ERROR_CONTENT)
        finally:
            DisplayManager.display_stack(MAIN_STACK)
            sleep(60)
