import cv2
import numpy as np

def remove_foreground():

    # Load input image
    img = cv2.imread("1.png")

    if img is None:
        print("Error: Image not found")
        return

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Example: Remove RED foreground
    # Red has two ranges in HSV

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create masks
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Invert mask (to keep everything except red foreground)
    mask_inv = cv2.bitwise_not(mask)

    # Remove foreground
    result = cv2.bitwise_and(img, img, mask=mask_inv)

    # Show results
    cv2.imshow("Original Image", img)
    cv2.imshow("Foreground Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call function
remove_foreground()
