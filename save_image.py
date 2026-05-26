import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg")  # Load image

if image is not None:

    img2 = cv2.resize(image, (800, 600))  # Resize image

    cv2.imwrite("output_picture.png", img2)  # Save image

    print("Image saved successfully!")

else:

    print("There is a problem.....")