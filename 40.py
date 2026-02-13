import cv2
import pytesseract

def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    extracted_text = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Extract text using OCR
        text = pytesseract.image_to_string(gray)
        
        if text.strip() != "":
            extracted_text += text + "\n"

    cap.release()
    return extracted_text


# Example usage
video_file = "video.mp4"
text_output = extract_text_from_video(video_file)

print("Extracted Text:")
print(text_output)
