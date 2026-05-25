import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg") #load image


if image is  not None:
    
    img2 = cv2.resize(image,(800,600)) #resize or reshape the picture

    
    print("image loaded")
    
    cv2.imshow("This is your image..." ,img2) #opening image 
    
    cv2.waitKey(0) #The image window remains open until the user clicks a button.
    
    cv2.destroyAllWindows() #for closing the image window
else:
    
    print("There is a problem.....")
    

