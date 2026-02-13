import cv2

def put_text_on_image():

    # Load input image
    img = cv2.imread("1.png")

    if img is None:
        print("Error: Image not found")
        return

    # Take text from user
    text = input("Enter the text to display on image: ")

    # Position of text (x, y)
    position = (50, 50)

    # Font style
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Font scale
    font_scale = 1

    # Color (Green in BGR)
    color = (0, 255, 0)

    # Thickness
    thickness = 2

    # Add text to image
    cv2.putText(img, text, position, font, font_scale, color, thickness)

    # Show result
    cv2.imshow("Image with Text", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call function
put_text_on_image()
