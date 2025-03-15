import cv2
import numpy as np
from picamera2 import Picamera2

# Initialize the camera
picam2 = Picamera2()
width, height = 640, 480

# Create the preview configuration with the desired resolution
config = picam2.create_video_configuration(main={"size": (width, height)})

# Configure the camera
picam2.configure(config)

# Load the pre-trained Haar Cascade Classifier for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start the camera preview
picam2.start()

while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Convert the frame to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop over the faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Region of interest (ROI) for eyes detection inside the face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Loop over the eyes detected
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around the eyes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the resulting frame with face and eye rectangles
    cv2.imshow('Eye Detection', frame)

    # Break the loop when the 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close all OpenCV windows
picam2.stop()
cv2.destroyAllWindows()