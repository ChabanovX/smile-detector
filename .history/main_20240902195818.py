import cv2


# Pre-trained Haar cascades for face/smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')


fucking_great_video_cam_capture = cv2.VideoCapture(1)

# Check for camera avail
if not fucking_great_video_cam_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()


while True:
    # Capture frame-by-frame
    ret, frame = fucking_great_video_cam_capture.read()

    # Another test 
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Convert the frame to grayscale (Haar cascades work better on grayscale images)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR_VNG)

    cv2.imshow("frame", frame)

    cv2.waitKey(1)

# fucking_great_video_cam_capture.release()
# cv2.destroyAllWindows()

