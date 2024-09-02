import cv2


# Pre-trained Haar cascades for face/smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')


# My (Yours) Video Camera
fucking_great_video_cam_capture = cv2.VideoCapture(1)

# Check for camera availability
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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Get the region of interest for smile detection
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Detect smiles
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=20, minSize=(25, 25))
        
        for (sx, sy, sw, sh) in smiles:
            # Draw a rectangle around the smile
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
            
            # Add text when a smile is detected
            cv2.putText(frame, 'Smile Detected!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
fucking_great_video_cam_capture.release()
cv2.destroyAllWindows()
