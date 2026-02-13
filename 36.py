import cv2
import numpy as np

def remove_background():

    # Load input image
    img = cv2.imread("1.png")

    if img is None:
        print("Error: Image not found")
        return

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define background color range (Example: Green background)
    lower_color = np.array([35, 40, 40])
    upper_color = np.array([85, 255, 255])

    # Create mask for background
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Invert mask (to keep foreground)
    mask_inv = cv2.bitwise_not(mask)

    # Apply mask to remove background
    result = cv2.bitwise_and(img, img, mask=mask_inv)

    # Show results
    cv2.imshow("Original Image", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Background Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call function
remove_background()
