#importing OpenCV library - Python
import cv2

# 1. Turning Images to grayScale
# flowersImage = cv2.imread('./images/colouredFlowers.jpeg')
# grayscaleFlowersImage = cv2.cvtColor(flowersImage, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Coloured to gray', grayscaleFlowersImage)

# 2. Blurring a image
# clearImage = cv2.imread('./images/ImageToBlur.jpeg')
# size = (5,5)
# blurredImage = cv2.blur(clearImage, size)
# cv2.imshow('clear to Blur Image', blurredImage)

# 3. Cropping an image
# originalImage = cv2.imread('./images/ImageToCrop.jpeg')
# print("shpe of the image ", originalImage.shape)
# croppedImage = originalImage[100:500, 200:900]
# cv2.imshow('cropped Image', croppedImage)

# 4. Shape analysis
shapesImage = cv2.imread('./images/shapes.jpeg')
gray = cv2.cvtColor(shapesImage, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(shapesImage, contours, -1, (0, 255, 0), 3)
cv2.imshow('shape detection', shapesImage)


# # 5. Flipping images
# imageToFlip = cv2.imread('./images/ImageToFlip.jpeg')
# flippedImage = cv2.flip(imageToFlip, 0)
# cv2.imshow('flipped an image', flippedImage)

# # 6. Face detection 
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#         # Load the image
# image = cv2.imread('./images/people.jpeg')
#     # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # Detect faces in the image
# faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# # Draw rectangles around the detected faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
# # Display the image with detected faces
# cv2.imshow('Face Detection', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
