import cv2

# Load your input image
img = cv2.imread("1.png")

if img is None:
    print("Error: Image not found")
else:
    height, width, _ = img.shape

    # Define center of circle (middle of image)
    center = (width // 2, height // 2)

    # Radius (1/4 of smaller dimension)
    radius = min(height, width) // 4

    # Color (Blue in BGR format)
    color = (255, 0, 0)

    # Thickness (-1 for filled circle)
    thickness = 3

    # Draw circle
    cv2.circle(img, center, radius, color, thickness)

    # Show result
    cv2.imshow("Circle on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
