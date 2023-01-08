from typing import Optional
from pygame import image, Surface, transform

k_BASE_ICON_PATH = "Visuals/images/weather_icons"
k_BASE_IMAGE_PATH = "Visuals/images/image_assets"
k_SCALE_FACTOR = 3


class ImageRenderer:
    """A class for generating image surfaces"""

    # @staticmethod
    # def weather_icon_surface(icon_filename: str) -> Surface:
    #     """Get a surface with the icon image on it"""
    #     path = os.path.join(k_BASE_ICON_PATH, icon_filename)
    #     surface = image.load(path)
    #     rect = surface.get_rect()
    #     surface = pygame.transform.smoothscale(surface, (rect.width*k_SCALE_FACTOR, rect.height*k_SCALE_FACTOR))
    #     return surface

    # @staticmethod
    # def image_surface(image_filename: str, max_width: int) -> Surface:
    #     """Get a surface with any image on it. Resizes images that are too wide for the screen"""
    #     path = os.path.join(k_BASE_IMAGE_PATH, image_filename)
    #     loaded_image = image.load(path)
    #     if loaded_image.get_rect().width > max_width:
    #         return ImageRenderer._scale_to_fit(loaded_image, max_width)
    #
    #     return loaded_image

    @staticmethod
    def image_surface(path_to_image: str, width: Optional[int] = None):
        loaded_image = image.load(path_to_image)
        if width:
            loaded_image = ImageRenderer._scale_to_fit(loaded_image, width)

        return loaded_image

    @staticmethod
    def _scale_to_fit(image_to_scale: Surface, target_width: int) -> Surface:
        """Scales an image to fit onto a screen width-wise"""
        # Target width / target height = Current width / current height
        # target height = target width * current height / current width
        image_rect = image_to_scale.get_rect()
        target_height = target_width * image_rect.height / image_rect.width
        return transform.scale(image_to_scale, (target_width, target_height))
