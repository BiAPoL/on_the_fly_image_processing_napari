import napari
import time
from napari._qt.qthreading import thread_worker

# create a viewer window
viewer = napari.Viewer()
viewer.grid

@viewer.bind_key("w")
def up(event):
    print("UP")

@viewer.bind_key("a")
def left(event):
    print("LEFT")

@viewer.bind_key("s")
def down(event):
    print("DOWN")

@viewer.bind_key("d")
def right(event):
    print("RIGHT")

# Start napari
napari.run()
