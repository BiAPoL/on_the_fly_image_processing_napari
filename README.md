# On the fly image processing with napari
This repository contains code examples and data for the "On-the-fly image processing session with Python and napari" session by [Robert Haase](https://physics-of-life.tu-dresden.de/bia) of the 
Smart Microscopy Workshop at the [Center for Cellular imaging at the University of Gothenbourg](https://www.gu.se/en/core-facilities/centre-for-cellular-imaging) in May 2021.

The slides are online available as well (soon).

The code examples are provided under the [unlicence](https://unlicense.org) which means you can freely reuse that code.

Big thanks goes to the [napari](https://napari.dev) commnunity for their excellent online tutorials and active support.

## Installation instructions

```
git clone https://github.com/BiAPoL/on_the_fly_image_processing_napari.git
cd on_the_fly_image_processing_napari
pip install -r requirements.txt
```

## Demos
* [Introduction to napari](http://nbviewer.jupyter.org/github/BiAPoL/on_the_fly_image_processing_napari/blob/master/01_napari.ipynb)
* [Interactive pixel classification using sckit-learn](http://nbviewer.jupyter.org/github/BiAPoL/on_the_fly_image_processing_napari/blob/master/02_interactive_pixel_classification_sklearn.ipynb)  
* [Key bindings](https://github.com/BiAPoL/on_the_fly_image_processing_napari/blob/master/03_key_bindings.py)
  * [ping pong](https://github.com/haesleinhuepf/natari/blob/master/napari_ping_pong.py)
* [Multi-threading](https://github.com/BiAPoL/on_the_fly_image_processing_napari/blob/master/04_threading_yield.py)
* [On-the-fly processing](https://github.com/BiAPoL/on_the_fly_image_processing_napari/blob/master/05_on_the_fly_processing.py)
* [Dock widgets](https://github.com/BiAPoL/on_the_fly_image_processing_napari/blob/master/06_dock_widgets.py)
* [Interactive measurements](https://github.com/BiAPoL/on_the_fly_image_processing_napari/blob/master/07_image_quality_display.py)
* [napari plugin example](https://github.com/haesleinhuepf/napari-image-quality-analyzer)
* [clEsperanto](http://nbviewer.jupyter.org/github/BiAPoL/on_the_fly_image_processing_napari/blob/master/09_clesperanto.ipynb)
  * [Benchmarking: Affine transforms in scipy, clEsperanto and cupy](https://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/affine_transforms.ipynb)

![](images/image_quality_napari.gif)

## See also
* [napari viewer tutorial](https://napari.org/tutorials/fundamentals/viewer.html)
* [napari image layer tutorial](https://napari.org/tutorials/fundamentals/image.html)
* [napari labels layer tutorial](https://napari.org/tutorials/fundamentals/labels.html)
* [Key bindings in napari](https://napari.org/guides/stable/connecting_events.html)
* [Multi-threading in napari](https://napari.org/guides/stable/threading.html)
* [Multi-dimensional image visualization in Python using napari [NEUBIAS Academy@Home] webinar](https://www.youtube.com/watch?v=VgvDSq5aCDQ)
