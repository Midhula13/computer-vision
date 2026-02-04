import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
image = cv2.imread('image.jpg')

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Step 4: Display original and equalized images
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original Grayscale Image")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Histogram Equalized Image")
plt.imshow(equalized, cmap='gray')
plt.axis('off')

plt.show()