import cv2
import time
from tqdm import tqdm

print("Welcome! This program allows you to convert an image into black and white and either display or save the result.")

image = input("Enter the image path:- ")

if image:

    print("Loading Image...")

    # 20 seconds loading animation
    for i in tqdm(range(1), desc="Loading", unit="sec"):
        time.sleep(1)

    read = cv2.imread(image)

    if read is not None:

        image2 = cv2.resize(read, (800, 600))

        print("Image loaded successfully..")

        user_input1 = input("Do you want to convert image into black and white:- ").lower()

        if user_input1 in ["yes", "yeap", "ofcourse"]:

            convert = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
            for i in tqdm(range(10),desc = "Loading",unit = "sec"):
                time.sleep(4)
                
                

            cv2.imshow("This is your black and white picture", convert)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        else:
            print("Can't find any image....")

else:
    print("No image path provided.")