import cv2

# Read the captured video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

print("Press 'n' for Normal speed")
print("Press 's' for Slow motion")
print("Press 'f' for Fast motion")
print("Press 'q' to Quit")

delay = 30  # Normal speed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('n'):       # Normal speed
        delay = 30
    elif key == ord('s'):     # Slow motion
        delay = 100
    elif key == ord('f'):     # Fast motion
        delay = 5
    elif key == ord('q'):     # Quit
        break

cap.release()
cv2.destroyAllWindows()