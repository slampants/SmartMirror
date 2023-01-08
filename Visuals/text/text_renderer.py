from pygame import font, Surface
from typing import Tuple

import os.path

k_ANTIALIAS = True
k_FONT_COLOR = (255, 255, 255)


class TextRenderer:
    """Handles all text rendering"""
    def __init__(self, font_name: str = "HelveticaNeue.ttc", font_size: int = 35):
        font_path = os.path.join("Visuals/text/fonts", font_name)
        self.fontRenderer = font.Font(font_path, font_size)

    def text_surface(self, text: str, color: Tuple[int, int, int] = k_FONT_COLOR) -> Surface:
        """Provides a surface for drawing from a provided string."""
        return self.fontRenderer.render(text, k_ANTIALIAS, color)
