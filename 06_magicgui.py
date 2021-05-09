import napari
from magicgui import magicgui
from napari.types import ImageData
from skimage.filters import gaussian
from skimage.io import imread

viewer = napari.Viewer()
blobs = imread('blobs.tif')
viewer.add_image(blobs)

@magicgui(call_button='Run')
def gaussian_blur(image : ImageData, sigma : float = 2) -> ImageData:
    """
    Apply a gaussian blur to an image.
    """
    return gaussian(image, sigma)

viewer.window.add_dock_widget(gaussian_blur)

napari.run()

