import cv2


# Pre-trained Haar cascades for face/smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

fucking_great_video_cam_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = fucking_great_video_cam_capture.read()
    
    # Convert the frame to grayscale (Haar cascades work better on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


