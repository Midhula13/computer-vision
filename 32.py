import cv2
import numpy as np

# Load existing image
img = cv2.imread("1.png")

if img is None:
    print("Image not found")
else:
    # Get image dimensions
    height, width, channels = img.shape

    # Box size = 1/10th of image size
    box_h = height // 10
    box_w = width // 10

    # Top-left corner → Black
    img[0:box_h, 0:box_w] = [0, 0, 0]

    # Top-right corner → Blue
    img[0:box_h, width-box_w:width] = [255, 0, 0]

    # Bottom-left corner → Green
    img[height-box_h:height, 0:box_w] = [0, 255, 0]

    # Bottom-right corner → Red
    img[height-box_h:height, width-box_w:width] = [0, 0, 255]

    # Show result
    cv2.imshow("Image with Colored Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
