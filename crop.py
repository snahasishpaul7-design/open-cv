import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg") #load image

if image is  not None:
    print("image loaded")
    
    crop = image[100:200,50:150] #first 100:200 is y means height or colum and after the comma second 50:150 is x means width or row 
    cv2.imshow("Cropped image is", crop)
    cv2.imshow("Original image is",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("There is a problem.....")
    
