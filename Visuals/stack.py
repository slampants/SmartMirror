from typing import List, Optional
from pygame import Rect, Surface

k_BG_COLOR = (0, 0, 0)


class Stack:
    """A class representing a stack of Surfaces to be rendered"""
    def __init__(self):
        self.surfaces: List[Surface] = []

    def add_to_stack(self, surfaces: List[Surface]):
        """Add a list of surfaces to the stack"""
        self.surfaces.extend(surfaces)

    def clear(self):
        self.surfaces.clear()

    def draw_stack_to_surface(self, draw_target: Surface):
        """Blit all items in the list to the screen, stacked in order, and clear the stack"""
        draw_target.fill(k_BG_COLOR)
        previous_surface_bottom: Optional[int] = None
        for surface in self.surfaces:
            current_rect: Rect = surface.get_rect()
            left, width, height = current_rect.left, current_rect.width, current_rect.height
            top = current_rect.top + previous_surface_bottom if previous_surface_bottom else current_rect.top
            new_rect = Rect(left, top, width, height)
            draw_target.blit(surface, new_rect)
            previous_surface_bottom = new_rect.height + new_rect.top

        self.surfaces.clear()
