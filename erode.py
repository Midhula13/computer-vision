import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('image (4).png')

# Step 2: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Create a kernel (3x3)
kernel = np.ones((3, 3), np.uint8)

# Step 4: Apply erosion
eroded = cv2.erode(gray, kernel, iterations=1)

# Step 5: Display images
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()