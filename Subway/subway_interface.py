from .subway_api import SubwayAPI
from .constants import k_SUBWAY_ICON_PATH
from Visuals.surface_generator import Surface, SurfaceGenerator


class SubwayInterface:
    """A class that provides an interface for the main application to get the visual content to display"""
    def __init__(self):
        self.api = SubwayAPI()

    def get_subway_content(self) -> [Surface]:
        """Gets all subway content for display and delivers it back to the caller as a single surface"""
        train_etas: [str] = self.api.get_subway_departure_strings()
        content: [Surface] = [
            SurfaceGenerator.text_surface("Next three trains:"),
            SurfaceGenerator.vertical_spacer()
        ]

        for eta in train_etas:
            content.append(self.create_subway_row(eta))

        return content

    @staticmethod
    def create_subway_row(departure_string: str) -> Surface:
        """Returns a surface with a train line logo on the left and an ETA on the right"""
        icon = SurfaceGenerator.image_surface(k_SUBWAY_ICON_PATH, 50)
        text = SurfaceGenerator.text_surface(departure_string)
        return SurfaceGenerator.merge_surfaces([icon, text])
