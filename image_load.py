import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg") #load image

if image is  not None:
    print("image loaded")
else:
    print("There is a problem.....")
    

