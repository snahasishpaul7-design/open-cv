import cv2

image = cv2.imread("beautiful-anime-character-cartoon-scene.jpg")

if image is not None:

    image = cv2.resize(image, (800, 600))

    print("\n===== COLOR CONVERSION MENU =====")
    print("1. Grayscale")
    print("2. RGB")
    print("3. HSV")
    print("4. LAB")
    print("5. YCrCb")
    print("6. HLS")
    print("7. XYZ")
    print("8. LUV")
    print("9. RGBA")
    print("10. Red Channel")
    print("11. Green Channel")
    print("12. Blue Channel")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        title = "Grayscale"

    elif choice == 2:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        title = "RGB"

    elif choice == 3:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        title = "HSV"

    elif choice == 4:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        title = "LAB"

    elif choice == 5:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        title = "YCrCb"

    elif choice == 6:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
        title = "HLS"

    elif choice == 7:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
        title = "XYZ"

    elif choice == 8:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
        title = "LUV"

    elif choice == 9:
        result = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        title = "RGBA"

    elif choice == 10:
        result = image.copy()
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        title = "Red Channel"

    elif choice == 11:
        result = image.copy()
        result[:, :, 0] = 0
        result[:, :, 2] = 0
        title = "Green Channel"

    elif choice == 12:
        result = image.copy()
        result[:, :, 1] = 0
        result[:, :, 2] = 0 #row column channel
        title = "Blue Channel"

    else:
        print("Invalid Choice!")
        exit()

    cv2.imshow(title, result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found!")