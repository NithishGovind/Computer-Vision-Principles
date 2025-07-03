import cv2
import numpy as np

def sequential_labeling(image):
    label = 1
    labeled = np.zeros_like(image, dtype=np.int32)
    label_equiv = {}

    def find(x):
        while label_equiv[x] != x:
            x = label_equiv[x]
        return x

    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            if image[i, j] == 255:
                neighbors = []
                if i > 0 and labeled[i-1, j] > 0:
                    neighbors.append(labeled[i-1, j])
                if j > 0 and labeled[i, j-1] > 0:
                    neighbors.append(labeled[i, j-1])

                if not neighbors:
                    labeled[i, j] = label
                    label_equiv[label] = label
                    label += 1
                else:
                    min_label = min(neighbors)
                    labeled[i, j] = min_label
                    for n in neighbors:
                        root1 = find(min_label)
                        root2 = find(n)
                        if root1 != root2:
                            label_equiv[root2] = root1

    # Second pass: resolve equivalences
    for i in range(rows):
        for j in range(cols):
            if labeled[i, j] > 0:
                labeled[i, j] = find(labeled[i, j])

    return labeled

if __name__ == "__main__":
    img = cv2.imread("bottle.jpg", cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    labeled_img = sequential_labeling(binary)
    normalized = (labeled_img * 255 / labeled_img.max()).astype(np.uint8)
    cv2.imwrite("sequential_labeling_output.png", normalized)
    print("Sequential labeling result saved.")
