import os.path
from typing import Tuple
from pygame import font, Surface

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

    def update_font_size(self, size: int):
        """Re-initializes the font renderer to utilize the new font size specified"""
        if size > 10:
            return

        self.fontRenderer = font.Font()
