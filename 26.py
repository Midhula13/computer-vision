import cv2

# Open input video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

frames = []

# Read all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Check if frames exist
if len(frames) == 0:
    print("No frames found in video")
    exit()

# Get video properties
height, width, layers = frames[0].shape
fps = 30

# Create output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("reversed_output.avi", fourcc, fps, (width, height))

# Play and save reversed frames
for frame in reversed(frames):

    cv2.imshow("Reversed Video", frame)
    out.write(frame)

    # Press Q to stop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

print("Reversed video completed!")
