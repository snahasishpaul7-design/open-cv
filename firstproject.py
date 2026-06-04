6
#This project converts a color image into a grayscale image by taking the image path as input from the user.
# The converted grayscale image can then be displayed on the screen or saved to a specified location.

import cv2

print("Welcome! This program allows you to convert an image into black and white and either display or save the result.")

print("press 1 display the black and white image")
print("press 2 save the black and white image")
print("press 3 both")
print("press 4 display colourful image")
print("press 5 save colourful image")
print("press 6 display and save colourful image")
print("press 7 do everything")

image = input("Enter the image path:- ")

if image:

    read = cv2.imread(image)

    if read is not None:

        image2 = cv2.resize(read, (800, 600))

        # convert is created here so it can be used everywhere
        convert = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        print("Image loaded successfully..")

        user_input1 = input("Do you want to convert image into black and white:- ").lower()

        if user_input1 in ["yes", "yeap", "ofcourse"]:

            user_input2 = input(
                "press 1 for display the black and white image\n"
                "press 2 for save the black and white image\n"
                "press 3 for both\n"
            )

            if user_input2 == "1":

                cv2.imshow("This is your black and white picture", convert)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            elif user_input2 == "2":

                cv2.imwrite("Output_image.png", convert)

                print("Image saved successfully..")

            elif user_input2 == "3":

                cv2.imshow("This is your black and white picture", convert)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                cv2.imwrite("Output_image.png", convert)

                print("Image saved successfully..")

            else:
                print("Invalid choice......please use just 1 2 or 3")

        elif user_input1 in ["no", "never", "nah"]:

            user_input3 = input(
                "Do you want to save or display the colourfull image\n"
                "For display colourful image press 4\n"
                "press 5 for save colourful image\n"
                "press 6 display and save colourful image:- "
            )

            if user_input3 == "4":

                cv2.imshow("This is your colourful image picture", image2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            elif user_input3 == "5":

                cv2.imwrite("Output_image.png", image2)

                print("Image saved successfully..")

            elif user_input3 == "6":

                cv2.imshow("This is your colourful picture", image2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                cv2.imwrite("Output_image.png", image2)

                print("Image saved successfully..")

            else:
                print("Invalid choice......please use just 4 5 or 6")

        user_input4 = input("Do you want to do everything:- ").lower()

        if user_input4 in ["yes", "yeap", "yea"]:

            cv2.imshow("This is your black and white picture", convert)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.imwrite("Black_and_White_Output.png", convert)

            print("Black and white image saved successfully..")

            cv2.imshow("This is your colourful picture", image2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.imwrite("Colourful_Output.png", image2)

            print("Colourful image saved successfully..")

        elif user_input4 in ["nah", "never", "no"]:
            exit()

        else:
            print("Invalid choice......")

    else:
        print("Can't find any image....")

else:
    print("Can't find any image....")

