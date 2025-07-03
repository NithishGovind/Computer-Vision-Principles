import cv2
import numpy as np
from collections import deque
input_img="bottle.jpg"

''''
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

If your binary image is too dark or too light, adjust the 127 value:

Use higher threshold (e.g., 180) to suppress lighter noise.

Use lower threshold (e.g., 80) to include lighter foreground regions.
'''
def region_growing(image, seed):
    rows, cols = image.shape
    segmented = np.zeros_like(image)
    visited = np.zeros_like(image, dtype=bool)

    q = deque([seed])
    visited[seed] = True
    segmented[seed] = 255

    while q:
        x, y = q.popleft()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if not visited[nx, ny] and image[nx, ny] == 255:
                        visited[nx, ny] = True
                        segmented[nx, ny] = 255
                        q.append((nx, ny))
    return segmented

if __name__ == "__main__":
    img = cv2.imread(input_img, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    seed = (100, 100)
    result = region_growing(binary, seed)
    
    cv2.imwrite("region_growing_output.png", result)
    print("Region growing result saved.")
