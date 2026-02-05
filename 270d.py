import cv2

# Read the image
image = cv2.imread("image (2).png")

# Rotate image by 270 degrees (clockwise)
rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display the result
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()