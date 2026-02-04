import cv2

# Step 1: Read the image
image = cv2.imread("image (2).png")

# Check if image is loaded
if image is None:
    print("Image not found")
else:
    # Step 2: Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Step 3: Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blurred Image", blurred_image)

    # Step 4: Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()