import napari
import time
from napari._qt.qthreading import thread_worker
import numpy as np

# create a viewer window
viewer = napari.Viewer()

# https://napari.org/guides/stable/threading.html
@thread_worker
def loop_run():
    while True: # endless loop
        print("Hello world", time.time())
        time.sleep(0.5)
        yield np.random.random((2, 2))


def update_layer(image):
    """
    Updates the image in the layer 'result'
    or adds this layer.
    """
    try:
        viewer.layers['result'].data = image
    except KeyError:
        viewer.add_image(image, name='result')

# Start the loop
worker = loop_run()
worker.yielded.connect(update_layer)
worker.start()

# Start napari
napari.run()
