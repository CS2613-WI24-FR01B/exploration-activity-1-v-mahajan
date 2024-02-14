# Exploration Activity - 1
# Submitted by - Vansh Mahajan
# Student ID - 3712178
# Course CS 2613
# Topic - Python Library : OpenCV 


# python Library import
import cv2

# 1. Turning Images to grayScale
flowersImage = cv2.imread('./images/colouredFlowers.jpeg')
grayscaleFlowersImage = cv2.cvtColor(flowersImage, cv2.COLOR_BGR2GRAY)
cv2.imshow('Coloured to gray', grayscaleFlowersImage)
cv2.moveWindow('Coloured to gray', 20, 20)

# 2. Blurring a image
clearImage = cv2.imread('./images/ImageToBlur.jpeg')
size = (20,20)
blurredImage = cv2.blur(clearImage, size)
cv2.imshow('clear to Blur Image', blurredImage)
cv2.moveWindow('clear to Blur Image', 40, 40)

# 3. Cropping an image
originalImage = cv2.imread('./images/ImageToCrop.jpeg')
print("shpe of the image ", originalImage.shape)
croppedImage = originalImage[100:500, 200:900]
cv2.imshow('cropped Image', croppedImage)
cv2.moveWindow('cropped Image', 60, 60)

# 4. Shape analysis
shapesImage = cv2.imread('./images/shapes.jpeg')
gray = cv2.cvtColor(shapesImage, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
contours, tempHeir = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    epsilon = 0.03 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.drawContours(shapesImage, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if (len(approx) == 3):
        cv2.putText( shapesImage, "Triangle", (x+45, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0) )

    elif (len(approx) == 4) :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(shapesImage, "Square", (x+ 50, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

        else:
            cv2.putText(shapesImage, "Rectangle", (x+50, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5 :
        cv2.putText(shapesImage, "pentagon", (x+50, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(shapesImage, "circle", (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv2.imshow('shape detection', shapesImage)
    cv2.moveWindow('shape detection', 80, 80)


# # 5. Flipping images
imageToFlip = cv2.imread('./images/ImageToFlip.jpeg')
flippedImage = cv2.flip(imageToFlip, 0)
cv2.imshow('flipped an image', flippedImage)
cv2.moveWindow('flipped an image', 100, 100)

# # 6. Face detection 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Load the image
groupImage = cv2.imread('./images/people.jpeg')
# Convert the image to grayscale
grayScaleImage = cv2.cvtColor(groupImage, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = face_cascade.detectMultiScale(grayScaleImage, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))
# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(groupImage, (x, y), (x+w, y+h), (0, 255, 0), 2)
# Display the image with detected faces
cv2.imshow('Face Detection', groupImage)
cv2.moveWindow('Face Detection', 120, 120)


cv2.waitKey(0)
cv2.destroyAllWindows()
