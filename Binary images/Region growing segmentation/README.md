# Region Growing Segmentation in Binary Images

This script performs **region growing segmentation** on a binary image using a seed point. It identifies connected components by expanding from a starting pixel and including neighboring pixels that meet the criteria.

---

### What is Region Growing?

Region growing is a pixel-based image segmentation technique. Starting from a *seed point*, it adds neighboring pixels with similar properties (here, intensity 255) to form a connected region.

### How It Works

1. **Input**: A binary image and a seed coordinate.
2. **Expansion**: The algorithm explores 8-connected neighbors.
3. **Inclusion Condition**: Pixels with intensity `255` are added to the growing region.

This method is simple but effective for separating objects from background when thresholding is already applied.

---

## Techniques Used

- **Thresholding**: Converts grayscale to binary using [`cv2.threshold`](https://docs.opencv.org/4.x/d7/d1b/tutorial_py_thresholding.html). You can tune the threshold value depending on image brightness.

  ```python
  _, binary = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
  ```

- **Region Growing**: Implements a custom flood-fill using a queue (`collections.deque`) to track and grow the region.

- **8-connected Neighborhood Check**: Loops through all neighbors including diagonals using offsets `[-1, 0, 1]`.

---

## Example

### Input Image
![Original Image](bottle.jpg)

### Region-Grown Output
![Segmented Output](region_growing_output.png)

---

### Customization

To change the segmentation seed, modify this line:

```python
seed = (100, 100)
```

Make sure the seed lies inside the foreground region (white pixel in the binary image).
