import cv2

# Read the image
img = cv2.imread('image (3).png')

if img is None:
    print("Error: Image not found")
    exit()

# Split BGR channels
b, g, r = cv2.split(img)

# Calculate histograms
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Analyze histogram values
print("Color Histogram Analysis")
print("Blue Channel - Max Pixel Count:", int(hist_b.max()))
print("Green Channel - Max Pixel Count:", int(hist_g.max()))
print("Red Channel - Max Pixel Count:", int(hist_r.max()))

# Display image
cv2.imshow("Input Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()