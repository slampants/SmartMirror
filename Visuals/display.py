from .stack import Stack
from pygame import Surface, transform
import pygame


class Display:
    """Class for handling the actual display of content. Ignorant of the nature of the content."""
    def __init__(self, screen_width: int, screen_height: int, screen_is_rotated: bool = True):
        self.screen: Surface = pygame.display.set_mode((screen_width, screen_height))
        self.screen_is_rotated = screen_is_rotated

    # def refresh(self, content: Surface, should_rotate: bool = True):
    #     """Updates the screen contents"""
    #     if should_rotate:
    #         content = pygame.transform.rotate(content, 90)
    #
    #     self.screen.blit(content, content.get_rect())

    def display_stack(self, stack: Stack):
        """Displays the contents of a stack on the screen"""
        # Create an intermediary surface
        screen_rect = self.screen.get_rect()
        buffer_surface_width = screen_rect.height if self.screen_is_rotated else screen_rect.width
        buffer_surface_height = screen_rect.width if self.screen_is_rotated else screen_rect.height
        buffer_surface = Surface((buffer_surface_width, buffer_surface_height))

        # Draw all content to the intermediary surface
        stack.draw_stack_to_surface(buffer_surface)
        if self.screen_is_rotated:
            buffer_surface = transform.rotate(buffer_surface, 90)

        # Blit to the screen and show it
        self.screen.blit(buffer_surface, self.screen.get_rect())
        pygame.display.flip()
