from .text.alignment import Alignment
from datetime import datetime
from typing import List
from Visuals.surface_generator import Surface, SurfaceGenerator


class TimeContent:
    """Class for displaying time information on screen"""

    @staticmethod
    def get_time_string() -> str:
        """Get the string representation for the current time"""
        return datetime.now().time().strftime("%H:%M")

    @staticmethod
    def get_time_surface() -> List[Surface]:
        """Gets the current time as a surface to display"""
        return [
            SurfaceGenerator.text_surface(TimeContent.get_time_string(), alignment=Alignment.CENTER, is_big=True),
            SurfaceGenerator.vertical_spacer(20)
        ]
