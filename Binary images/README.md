# Binary Image Operations

This repository contains a collection of classic binary image processing techniques implemented in Python using OpenCV. These techniques are fundamental in computer vision tasks such as object segmentation, shape analysis, and connected component labeling.

---

## Contents

### 📁 [Roundedness](Roundedness/)
Measure the circularity of each region in a binary image using the formula:

```
Roundedness = (4 × π × Area) / (Perimeter²)
```

A higher value indicates a more circular shape. This is useful for filtering round objects or characterizing shape irregularities.

➡ See: [Roundedness/README.md](Roundedness/README.md)

---

### 📁 [Region Growing Segmentation](Region%20growing%20segmentation/)
A simple pixel-based segmentation technique starting from a seed point and expanding to include connected pixels based on intensity. Works well when foreground and background are separated by thresholding.

➡ See: [Region growing segmentation/README.md](Region%20growing%20segmentation/README.md)

---

### 📁 [Sequential Labelling Algorithm](Sequential%20labelling%20algorithm/)
Implements the two-pass connected-component labeling algorithm to identify and label each connected foreground region with a unique identifier. Useful for counting objects or filtering specific regions.

➡ See: [Sequential labelling algorithm/README.md](Sequential%20labelling%20algorithm/README.md)

---

## Requirements

All subprojects use:
- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://numpy.org/)

Install dependencies using:

```bash
pip install opencv-python numpy
```

---

This collection is useful for anyone learning binary image processing fundamentals or building pre-processing pipelines for vision tasks.
