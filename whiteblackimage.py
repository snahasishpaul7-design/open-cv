import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg")

if image is not None:
    im = cv2.resize(image,(800,600))
    
    
    wb = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #convert the image into black and white must use cvtcolor
    
    cv2.imshow("image is",wb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nothing found")