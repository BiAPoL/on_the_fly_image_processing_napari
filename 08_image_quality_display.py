import napari
import time

from napari import Viewer
from napari._qt.qthreading import thread_worker
from qtpy.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
import numpy as np

def determine_quality(image):
    """
    Computes quality of an image as single number.
    """
    return np.std(image)

viewer = napari.Viewer()

class ImageQualityPanel(QWidget):
    """
    The image quality panel is a Widget in the user interface that
    shows visually how high the image quality is at the moment.
    """
    def __init__(self, napari_viewer: Viewer):

        super().__init__(napari_viewer.window.qt_viewer)
        self._viewer = napari_viewer

        self.setObjectName("Image quality")

        # setup user interface
        self.label = QLabel("0")
        font = self.label.font()
        font.setPointSize(30)
        self.label.setFont(font)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self._reset)

        self.setLayout(QHBoxLayout(self))
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.reset_button)
        self.layout().addStretch()

        # initial state
        self._reset()

        # threading
        # https://napari.org/guides/stable/threading.html
        @thread_worker
        def loop_run():
            while True: # endless loop
                # get currently active layer
                selected_layers = self._viewer.layers.selection
                if len(selected_layers) > 0:
                    # measure quality and update GUI
                    quality = determine_quality(selected_layers.active.data)
                    self._update_quality(quality)

                time.sleep(0.1)
                yield

        # Start the loop
        worker = loop_run()
        worker.start()

    def _reset(self):
        self.best_quality = 0

    def _update_quality(self, quality):
        """
        Updates the image quality display
        """
        if self.best_quality < quality:
            self.best_quality = quality

        # put current quality in label
        self.label.setText(str(quality)[0:5])

        # color label according to quality
        ratio_to_best = quality / self.best_quality
        if ratio_to_best > 0.9:
            self.label.setStyleSheet("QLabel { color : green }")
        elif ratio_to_best > 0.5:
            self.label.setStyleSheet("QLabel { color : yellow }")
        else:
            self.label.setStyleSheet("QLabel { color : red }")

viewer.window.add_dock_widget(ImageQualityPanel(viewer), area='right')

# Start napari
napari.run()
