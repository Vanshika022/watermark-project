'''import cv2
import face_recognition

# Load the image and convert it to RGB
image = cv2.imread("path_to_image.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detect faces in the image
face_locations = face_recognition.face_locations(rgb_image)

# Loop through each detected face
for (top, right, bottom, left) in face_locations:
    # Draw a rectangle around the face
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Mark attendance or perform any other action here
    # ...

# Display the image with detected faces
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
import cv2
import numpy as np
import face_recognition_models
import face_recognition
imgElon=face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)
