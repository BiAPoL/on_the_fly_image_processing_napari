import napari
from qtpy.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSpinBox
import numpy as np

viewer = napari.Viewer()

class AddImageWidget(QWidget):
    """
    This widget allows to create new random images
    """
    def __init__(self, napari_viewer: napari.Viewer):
        super().__init__()
        # configure widget
        self._viewer = napari_viewer
        self.setObjectName("Add image")

        # setup user interface
        self.width_spinner = QSpinBox()
        self.width_spinner.setValue(50)
        self.height_spinner = QSpinBox()
        self.height_spinner.setValue(50)

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self._create)

        # put spinners and buttons in the user interface
        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self.width_spinner)
        self.layout().addWidget(self.height_spinner)
        self.layout().addWidget(self.create_button)
        self.layout().addStretch()

    def _create(self):
        """
        Create a new image and add it to the viewer
        """
        image = np.random.random((self.height_spinner.value(), self.width_spinner.value()))
        self._viewer.add_image(image)

# add the dock widget to the viewer
viewer.window.add_dock_widget(AddImageWidget(viewer), area='right')

# Start napari
napari.run()
