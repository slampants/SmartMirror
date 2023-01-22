from .constants import k_SCREEN_HEIGHT
from .images.image_renderer import ImageRenderer
from .text.alignment import Alignment
from .text.text_renderer import TextRenderer
from pygame import Surface

# Setting to screen height under assumption that screen is rotated. Change this if necessary
k_CONTENT_WIDTH = k_SCREEN_HEIGHT


class SurfaceGenerator:
    """Static class for generating surfaces for text and images"""
    @staticmethod
    def text_surface(text: str, max_width: int = k_CONTENT_WIDTH, alignment: Alignment = Alignment.LEFT) -> Surface:
        """Returns a text surface"""
        return TextRenderer().text_surface(text, alignment=alignment)

    @staticmethod
    def image_surface(filepath: str, max_width: int = k_CONTENT_WIDTH) -> Surface:
        """Returns an image surface"""
        return ImageRenderer.image_surface(filepath, max_width)

    @staticmethod
    def spacer(height: int = 10) -> Surface:
        return Surface((k_CONTENT_WIDTH, height))
