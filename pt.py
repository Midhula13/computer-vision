import cv2
import numpy as np

# Read the image
image = cv2.imread("image (2).png")

# Get image dimensions
rows, cols = image.shape[:2]

# Define source points (from original image)
pts1 = np.float32([
    [50, 50],
    [cols - 50, 50],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Define destination points (perspective change)
pts2 = np.float32([
    [0, 0],
    [cols, 0],
    [100, rows],
    [cols - 100, rows]
])

# Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective_image)
cv2.waitKey(0)
cv2.destroyAllWindows()