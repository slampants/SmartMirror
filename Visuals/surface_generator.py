from .constants import k_SCREEN_HEIGHT
from .images.image_renderer import ImageRenderer
from .text.alignment import Alignment
from .text.text_renderer import TextRenderer
from functools import reduce
from pygame import Surface
from typing import Optional

# Setting to screen height under assumption that screen is rotated. Change this if necessary
k_CONTENT_WIDTH = k_SCREEN_HEIGHT


class SurfaceGenerator:
    """Static class for generating surfaces for text and images"""
    @staticmethod
    def text_surface(text: str, max_width: int = k_CONTENT_WIDTH, alignment: Alignment = Alignment.LEFT,
                     is_big: bool = False) -> Surface:
        """Returns a text surface"""
        if is_big:
            return TextRenderer().big_text_surface(text, alignment=alignment)
        else:
            return TextRenderer().text_surface(text, alignment=alignment)

    @staticmethod
    def image_surface(filepath: str, max_width: int = k_CONTENT_WIDTH) -> Surface:
        """Returns an image surface"""
        return ImageRenderer.image_surface(filepath, max_width)

    @staticmethod
    def vertical_spacer(height: int = 10) -> Surface:
        return Surface((k_CONTENT_WIDTH, height))

    @staticmethod
    def merge_surfaces(surfaces: [Surface], width: int = k_CONTENT_WIDTH, height: Optional[int] = None) -> Surface:
        """
        Takes a list of surfaces and merges them into a single surface, justified to spread across a given width.
        This will clip horizontally if there is not room for all surfaces to fit end-to-end

        Args:
        :param surfaces: A list of two or more surfaces to merge
        :param width: The width of the space to merge into
        :param height: Height to constrain the merged surface to. If None, constrains to tallest surface provided

        :return: A single surface
        """

        # If a height value is not provided, we choose the height of the tallest surface provided
        if not height:
            height = max(surfaces, key=lambda surface: surface.get_height()).get_height()

        resultant_surface = Surface((width, height))

        # Get the amount of padding needed between elements
        surfaces_total_width = reduce(lambda x, y: x + y.get_width(), surfaces, 0)
        padding_size = width - surfaces_total_width

        surfaces_index = 0
        blit_x_value = 0
        # While you've still got horizontal room and you haven't iterated through all surfaces yet
        while blit_x_value < width and surfaces_index < len(surfaces):
            # blit onto the surface
            next_surface: Surface = surfaces[surfaces_index]
            resultant_surface.blit(next_surface, (blit_x_value, 0))
            blit_x_value = blit_x_value + padding_size + next_surface.get_width()
            surfaces_index += 1

        return resultant_surface
