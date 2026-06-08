import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg")

if image is not None:
    
    img= cv2.resize(image, (800, 600))
    
    #cv2.flip(variable,flipole)
    
    flipped = cv2.flip(img,0) # 0 means top to bottom and 1 means horizontal to vertical and -1 is both
    
    cv2.imshow("This is your flipped image",flipped)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
else:
    print("Image not found......")