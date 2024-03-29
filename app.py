from requests import ConnectionError
from time import sleep
from Subway.subway_interface import SubwayInterface
from Visuals.time_content import TimeContent
from Visuals.constants import *
from Visuals.display import Display
from Visuals.error_content import ErrorContent
from Visuals.stack import Stack
from Weather.weather_interface import WeatherManager

import pygame

pygame.init()
pygame.mouse.set_visible(False)

WEATHERMAN = WeatherManager()
TRAIN_CONDUCTOR = SubwayInterface()
MAIN_STACK = Stack()
ERROR_CONTENT = ErrorContent.get_error_content()
DisplayManager = Display(k_SCREEN_WIDTH, k_SCREEN_HEIGHT)

if __name__ == "__main__":
    while True:
        MAIN_STACK.add_to_stack(TimeContent.get_time_surface())
        try:
            weather_content = WEATHERMAN.get_weather_content()
            MAIN_STACK.add_to_stack(weather_content)
            subway_content = TRAIN_CONDUCTOR.get_subway_content()
            MAIN_STACK.add_to_stack(subway_content)
        except ConnectionError:
            MAIN_STACK.add_to_stack(ERROR_CONTENT)
        finally:
            DisplayManager.display_stack(MAIN_STACK)
            sleep(60)
