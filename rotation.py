import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg")

if image is not None:
    
    img= cv2.resize(image, (800, 600))
    
    (h,w) = img.shape[:2]
    
    
    center = (w//2 ,h//2)
    
    M =cv2.getRotationMatrix2D(center,90,1.0)
    
    rotated = cv2.warpAffine(img,M ,(w,h))
    
    cv2.imshow("Original image is",img)
    
    cv2.imshow("Rotating image is", rotated)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
else:
    print("Image not found......")