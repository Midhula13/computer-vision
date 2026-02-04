import cv2

# Step 1: Read the image
image = cv2.imread("image (3).png")   # replace with your image name

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Step 4: Show images
cv2.imshow("Original Image", image)
cv2.imshow("Outline using Canny", edges)

# Step 5: Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()