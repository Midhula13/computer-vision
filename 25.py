import cv2
import numpy as np

# Load image
img = cv2.imread("image 1.png")

# Check if image loaded
if img is None:
    print("Error: Image not found")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply blur
    gray = cv2.GaussianBlur(gray, (9, 9), 0)

    # Detect circles
    circles = cv2.HoughCircles(gray,
                               cv2.HOUGH_GRADIENT,
                               1,
                               100)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            # Draw outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 3)

            # Draw center
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        print("Watch Detected")

    else:
        print("Watch Not Detected")

    # Show result
    cv2.imshow("Watch Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
