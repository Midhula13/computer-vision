import cv2

# Load your input image
img = cv2.imread("1.png")

if img is None:
    print("Error: Image not found")
else:
    height, width, _ = img.shape

    # Define rectangle coordinates (center area)
    start_point = (width // 4, height // 4)
    end_point = (3 * width // 4, 3 * height // 4)

    # Rectangle color (Green in BGR)
    color = (0, 255, 0)

    # Thickness (use -1 for filled rectangle)
    thickness = 3

    # Draw rectangle
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Show result
    cv2.imshow("Rectangle on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
