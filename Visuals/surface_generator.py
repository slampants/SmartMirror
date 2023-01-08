from .text.text_renderer import TextRenderer
from .images.image_renderer import ImageRenderer
from .constants import k_SCREEN_HEIGHT
from pygame import Surface

# Setting to screen height under assumption that screen is rotated. Change this if necessary
k_CONTENT_WIDTH = k_SCREEN_HEIGHT


class SurfaceGenerator:
    """Static class for generating surfaces for text and images"""
    @staticmethod
    def text_surface(text: str, max_width: int = k_CONTENT_WIDTH) -> Surface:
        """Returns a text surface"""
        return TextRenderer().text_surface(text)

    # @staticmethod
    # def icon_surface(self, filename: str) -> Surface:
    #     """Returns an icon surface"""
    #     return ImageRenderer.weather_icon_surface(filename)

    @staticmethod
    def image_surface(filepath: str, max_width: int = k_CONTENT_WIDTH) -> Surface:
        """Returns an image surface"""
        return ImageRenderer.image_surface(filepath, max_width)
