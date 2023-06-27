from .surface_generator import Surface, SurfaceGenerator
from .text.text_renderer import Alignment
from typing import List


class ErrorContent:
    """This class generates error-oriented content"""

    @staticmethod
    def error_image() -> Surface:
        """Returns the error image"""
        return SurfaceGenerator.image_surface("Visuals/images/weather_icons/error.png")

    @staticmethod
    def error_message() -> Surface:
        """Returns a generic text message centered on a surface"""
        return SurfaceGenerator.text_surface("No data available", alignment=Alignment.CENTER)

    @staticmethod
    def get_error_content() -> List[Surface]:
        """Returns a list containing the two error elements"""
        return [
            ErrorContent.error_image(),
            SurfaceGenerator.vertical_spacer(40),
            ErrorContent.error_message()
        ]
