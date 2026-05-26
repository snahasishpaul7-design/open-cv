import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg")

if image is not None:
    
    img= cv2.resize(image, (800, 600))  # Resize image
    
    h,w,c = img.shape # with this attribute you can find the height width and colour of your using picture 
    
    print(f"Height is {h}\n width is {w}\n colour channel is {c}")
else:
    
    print("There is no image ")