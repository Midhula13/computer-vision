import cv2

def count_faces(image_path):
    # Load the Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Read the image
    img = cv2.imread(image_path)

    # Check if image loaded successfully
    if img is None:
        print("Error: Unable to load image.")
        return 0

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Return number of faces detected
    return len(faces)


# Example usage
image = "1.png"
face_count = count_faces(image)
print("Number of faces detected:", face_count)
