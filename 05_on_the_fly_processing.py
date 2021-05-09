import napari
import time
from napari._qt.qthreading import thread_worker
from cv2.cv2 import VideoCapture
from napari.layers import Labels
from skimage.color import rgb2gray
import numpy as np
from skimage import draw

camera_index = 0

def acquire_image(camera : VideoCapture):
    """
    Acquires an image from a given camera
    """

    # acquire image
    _, picture = camera.read()
    if picture is None:
        return

    # convert to single channel image
    return rgb2gray(picture)

def update_layers(images_data : dict):
    """
    Add images to napari is layer or updates a pre-existing layer
    """
    for name in images_data.keys():
        image = images_data[name]
        for layer in viewer.layers:
            if layer.name == name:
                if isinstance(layer, Labels):
                    layer.data = image.astype(int)
                else:
                    layer.data = image
                image = None
                break

        if image is not None:
            if 'labels' in name:
                viewer.add_labels(image.astype(int), name=name)
            else:
                viewer.add_image(image, name=name)

def process_image(image):

    # estimate maximum position
    from scipy.ndimage import center_of_mass
    y, x = center_of_mass(np.power(image, 100))

    # draw a circle around maximum
    rr, cc = draw.circle_perimeter(int(y), int(x), radius=10, shape=image.shape)
    circle_image = np.zeros(image.shape)
    circle_image[rr, cc] = 1

    # send dictionary of images back to napari
    return {
        "original" : image,
        "circle_labels" : circle_image
    }

# create a viewer window
viewer = napari.Viewer()

# connect to webcam
camera = VideoCapture(camera_index)

# https://napari.org/guides/stable/threading.html
@thread_worker
def loop_run():
    while viewer.window.qt_viewer:  # loop until napari closes
        image = acquire_image(camera)
        yield process_image(image)
        time.sleep(0.5)

    # stop acquisition
    camera.release()

# Start the loop
worker = loop_run()
worker.yielded.connect(update_layers)
worker.start()

# Start napari
napari.run()
