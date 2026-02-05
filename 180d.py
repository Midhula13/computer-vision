import cv2

# Read the image
image = cv2.imread("image (3).png")

# Rotate image by 180 degrees
rotated = cv2.rotate(image, cv2.ROTATE_180)

# Display the result
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()