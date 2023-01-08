from .text.text_renderer import TextRenderer
from .images.image_renderer import ImageRenderer
from pygame import Surface


class SurfaceGenerator:
    """Easy interface for generating surfaces"""
    def __init__(self, screen_width: int):
        self.text_renderer = TextRenderer()
        self.max_width = screen_width

    def text_surface(self, text: str) -> Surface:
        """Returns a text surface"""
        return self.text_renderer.text_surface(text)

    def icon_surface(self, filename: str) -> Surface:
        """Returns an icon surface"""
        return ImageRenderer.weather_icon_surface(filename)

    def image_surface(self, filename: str) -> Surface:
        """Returns an image surface"""
        return ImageRenderer.image_surface(filename, self.max_width)
