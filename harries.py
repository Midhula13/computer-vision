import cv2
import numpy as np

# Read the image
image = cv2.imread("image (2).png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate corners for better visibility
corners = cv2.dilate(corners, None)

# Mark detected corners in red
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display result
cv2.imshow("Harris Corner Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()