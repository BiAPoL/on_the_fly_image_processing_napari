import napari
import time
from napari._qt.qthreading import thread_worker
import numpy as np

# create a viewer window
viewer = napari.Viewer()

# https://napari.org/guides/stable/threading.html
@thread_worker
def loop_run():
    while viewer.window.qt_viewer:  # loop until napari closes
        print("Hello world", time.time())
        viewer.add_image(np.random.random((2, 2)))
        time.sleep(0.5)

# Start the loop
worker = loop_run()
worker.start()

# Start napari
napari.run()
