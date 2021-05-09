import napari

# create a viewer window
viewer = napari.Viewer()

# bind short cuts to functions
@viewer.bind_key("w")
def up(event):
    print("UP")

def left(event):
    print("LEFT")
viewer.bind_key("a", left)

@viewer.bind_key("s")
def down(event):
    print("DOWN")

@viewer.bind_key("d")
def right(event):
    print("RIGHT")

# Start napari
napari.run()
