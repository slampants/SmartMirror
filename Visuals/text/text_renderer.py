from pygame import font, Surface
from typing import List, Tuple
from ..constants import k_SCREEN_HEIGHT, k_MAIN_SIZE_CHARACTER_LIMIT
from ..stack import Stack

from enum import Enum
import os.path
from queue import LifoQueue

k_ANTIALIAS = True
k_FONT_COLOR = (255, 255, 255)


class Alignment(Enum):
    LEFT = 0
    CENTER = 1


class TextRenderer:
    """Handles all text rendering"""
    def __init__(self, font_name: str = "HelveticaNeue.ttc", font_size: int = 35):
        font_path = os.path.join("Visuals/text/fonts", font_name)
        self.fontRenderer = font.Font(font_path, font_size)

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

    def _get_aligned_rendering(
            self, text: str, anti_alias: bool = k_ANTIALIAS, color: Tuple[int, int, int] = k_FONT_COLOR,
            alignment: Alignment = Alignment.LEFT
    ) -> Surface:
        """Provides a surface that has text aligned as desired"""
        if alignment == Alignment.LEFT:
            return self.fontRenderer.render(text, anti_alias, color)
        elif alignment == Alignment.CENTER:
            # TODO: Implement!
            raise NotImplementedError("Not implemented!")

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

        result_surface: Surface = Surface((k_SCREEN_HEIGHT, total_height))
        rows_stack.draw_stack_to_surface(result_surface)
        return result_surface
