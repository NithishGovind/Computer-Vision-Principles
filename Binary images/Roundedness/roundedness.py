# Measure Roundedness in Binary Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
input_img="bottle.jpg"
def compute_roundedness(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        if perimeter == 0:
            continue
        roundedness = 4 * np.pi * area / (perimeter ** 2)
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0
        results.append({
            "region": i + 1,
            "area": area,
            "perimeter": perimeter,
            "roundedness": roundedness,
            "centroid": (cx, cy),
            "contour": cnt
        })
    return results

def visualize_roundedness(original_gray, results):
    color_img = cv2.cvtColor(original_gray, cv2.COLOR_GRAY2BGR)
    for r in results:
        cv2.drawContours(color_img, [r["contour"]], -1, (0, 255, 0), 2)
        cx, cy = r["centroid"]
        cv2.putText(color_img, f"R={r['roundedness']:.2f}", (cx-30, cy), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    
    # Show using matplotlib
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
    
    plt.title("Roundedness of Each Region")
    plt.axis('off')
    plt.show()
    
if __name__ == "__main__":
    # Load and threshold image
    img = cv2.imread(input_img, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    results = compute_roundedness(binary)
    for r in results:
        print(f"Region {r['region']}: Area={r['area']:.1f}, Perimeter={r['perimeter']:.1f}, Roundedness={r['roundedness']:.3f}")

    visualize_roundedness(binary, results)
