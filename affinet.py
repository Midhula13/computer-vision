import cv2
import numpy as np

# Read the image
image = cv2.imread("image (2).png")

# Get image dimensions
rows, cols = image.shape[:2]

# Define points for affine transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine_image = cv2.warpAffine(image, matrix, (cols, rows))

# Display the result
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", affine_image)
cv2.waitKey(0)
cv2.destroyAllWindows()