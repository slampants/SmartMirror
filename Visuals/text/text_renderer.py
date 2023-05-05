from pygame import font, Surface
from typing import List, Tuple
from .alignment import Alignment
from ..constants import k_SCREEN_HEIGHT, k_MAIN_SIZE_CHARACTER_LIMIT
from ..stack import Stack

import os.path
from queue import LifoQueue

k_ANTIALIAS = True
k_FONT_COLOR = (255, 255, 255)
k_CONTENT_WIDTH = k_SCREEN_HEIGHT


class TextRenderer:
    """Handles all text rendering"""
    def __init__(self, font_name: str = "HelveticaNeue.ttc", font_size: int = 35):
        font_path = os.path.join("Visuals/text/fonts", font_name)
        self.fontRenderer = font.Font(font_path, font_size)
        self.bigFontRenderer = font.Font(font_path, 75)

    def text_surface(self, text: str, color: Tuple[int, int, int] = k_FONT_COLOR,
                     alignment: Alignment = Alignment.LEFT) -> Surface:
        """
        Provides a surface from a provided string. Automatically performs the equivalent of line wrapping
        """
        if len(text) <= k_MAIN_SIZE_CHARACTER_LIMIT:
            return self._get_aligned_rendering(text, alignment=alignment)

        rows: [str] = self._wrap_text_to_rows(text)
        final_surface = self._rows_to_single_surface(rows, alignment=alignment)
        return final_surface

    def big_text_surface(self, text: str, color: Tuple[int, int, int] = k_FONT_COLOR,
                         alignment: Alignment = Alignment.CENTER) -> Surface:
        """Provides a surface with large text, centered"""
        return self._get_aligned_rendering(text, alignment=alignment, is_big=True)

    def _get_aligned_rendering(
            self, text: str, anti_alias: bool = k_ANTIALIAS, color: Tuple[int, int, int] = k_FONT_COLOR,
            alignment: Alignment = Alignment.LEFT, is_big: bool = False
    ) -> Surface:
        """Provides a surface that has text aligned as desired"""
        renderer = self.bigFontRenderer if is_big else self.fontRenderer
        if alignment == Alignment.LEFT:
            return renderer.render(text, anti_alias, color)
        elif alignment == Alignment.CENTER:
            rendered_text = renderer.render(text, anti_alias, color)
            width = k_CONTENT_WIDTH
            height = rendered_text.get_rect().height
            return self._centered_on_empty_surface(rendered_text, width, height)

    @staticmethod
    def _centered_on_empty_surface(surface_to_center: Surface, target_width: int, target_height: int) -> Surface:
        """Returns new surface with the passed-in surface centered on a blank surface of target_width x target_height"""
        if surface_to_center.get_rect().width > target_width:
            raise ValueError("Cannot center a surface onto a new surface of lesser width")

        new_surface: Surface = Surface((target_width, target_height))
        # How much empty space there is, laterally, at the end of the supplied surface on this new surface
        empty_space: int = target_width - surface_to_center.get_rect().width
        # To center it, simply place the leading edge at a value half of the empty space
        leading_edge_value: int = empty_space // 2
        new_surface.blit(surface_to_center, (leading_edge_value, 0))
        return new_surface

    @staticmethod
    def _wrap_text_to_rows(text: str) -> List[str]:
        """
        Takes a string that is too long to display and splits it into a list of strings that are each within the line
        character length limit.
        """

        rows: [str] = []
        words: [str] = text.split()
        words.reverse()
        words_queue: LifoQueue = LifoQueue()
        for word in words:
            words_queue.put(word)

        row: str = ""
        while not words_queue.qsize() == 0:
            next_word: str = words_queue.get()
            if len(next_word) + len(row) <= k_MAIN_SIZE_CHARACTER_LIMIT:
                row = row + next_word + " "
            else:
                # Put the word back in the stack
                words_queue.put(next_word)
                rows.append(row)
                row = ""

        # Might have a row left!
        if row != "":
            rows.append(row)

        return rows

    def _rows_to_single_surface(self, rows: List[str], alignment: Alignment = Alignment.LEFT) -> Surface:
        """Renders a list of rows of text into a single surface and returns the surface."""
        total_height: int = 0
        rows_stack = Stack()
        for row in rows:
            row_surface = self._get_aligned_rendering(row, alignment=alignment)
            total_height += row_surface.get_rect().height
            rows_stack.add_to_stack([row_surface])

        result_surface: Surface = Surface((k_CONTENT_WIDTH, total_height))
        rows_stack.draw_stack_to_surface(result_surface)
        return result_surface
