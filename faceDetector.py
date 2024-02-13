#importing OpenCV library - Python
import cv2

# 1. Turning Images to grayScale
flowersImage = cv2.imread('./images/colouredFlowers.jpeg')
grayscaleFlowersImage = cv2.cvtColor(flowersImage, cv2.COLOR_BGR2GRAY)
cv2.imshow('Coloured to gray', grayscaleFlowersImage)

# 2. Blurring a image
clearImage = cv2.imread('./images/ImageToBlur.jpeg')
size = (5,5)
blurredImage = cv2.blur(clearImage, size)
cv2.imshow('clear to Blur Image', blurredImage)

# 3. Cropping an image

# 4. Shape analysis

# 5. Flipping images

# 6. Face detection 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image = cv2.imread('./images/people.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with detected faces
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()