
#CV2.CIRCLE(IMG,CENTER,RADIUS,COLOR,THICKNESS)

import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg") #load image


if image is  not None:
    
    img2 = cv2.resize(image,(800,600)) #resize or reshape the picture

    
    print("image loaded")
    
    center = 150,150
    
    radius = 50
    
    color = (0,255,255)
    
    thickness = 5
    
    cv2.circle(img2,center,radius,color,thickness)
    
    cv2.imshow("This is your image..." ,img2) #opening image 
    
    cv2.waitKey(0) #The image window remains open until the user clicks a button.
    
    cv2.destroyAllWindows() #for closing the image window
else:
    
    print("There is a problem.....")
    
