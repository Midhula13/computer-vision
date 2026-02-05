import cv2

# Read the image
image = cv2.imread("image (3).png")

# Resize to smaller size
small_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Resize to bigger size
large_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Smaller Image", small_image)
cv2.imshow("Bigger Image", large_image)

cv2.waitKey(0)
cv2.destroyAllWindows()