import cv2

# Load image
img = cv2.imread("1.png")

if img is None:
    print("Error: Image not found")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Given threshold value (change if needed)
    threshold_value = 127

    # Apply threshold segmentation
    ret, segmented = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Segmented Image", segmented)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
