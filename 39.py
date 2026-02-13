import cv2

def play_reverse_slow(video_path):
    # Capture video
    cap = cv2.VideoCapture(video_path)
    
    frames = []

    # Read all frames and store them
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Play frames in reverse order (slow motion)
    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)
        
        # Increase delay for slow motion (e.g., 100 ms)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


# Example usage
video_file = "video.mp4"
play_reverse_slow(video_file)
