import cv2

image = input("Enter the image path:- ")

image1 = cv2.imread(image)


if image1 is None:
    print("Image not found!")
else:
    img2 = cv2.resize(image1, (800, 600))
    
    while True:

        user_0 = input(
            "\nDo you want to show the original image? (yes/no/exit):- "
        ).lower()

        if user_0 in ["yes", "yeap", "yea"]:

            cv2.imshow("Your image is:-", img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif user_0 == "no":
            
            

            user_1 = input(
                "\nWhich operation do you want?\n"
                "Press 0 to change the size of picture\n"
                "Press 1 to draw line in image\n"
                "Press 2 to draw circle in image\n"
                "Press 3 to rotate the image\n"
                "Press 4 to flip the image\n"
                "Press 5 to to draw a rectangle in image\n"
                "press 6 to write any text in image\n"
                "Choice:- "
            )

            # Resize
            if user_1 == "0":

                value1 = int(input("Enter width (px):- "))
                value2 = int(input("Enter height (px):- "))

                im2 = cv2.resize(image1, (value1, value2))

                cv2.imshow("Your image is:-", im2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            # Draw Line
            elif user_1 == "1":

                lin_count = int(input("How many lines do you need:- "))

                for i in range(lin_count):

                    print(f"\nLine {i + 1}")

                    x1 = int(input("Enter x1:- "))
                    y1 = int(input("Enter y1:- "))

                    x2 = int(input("Enter x2:- "))
                    y2 = int(input("Enter y2:- "))

                    thickness = int(input("Enter the thickness:- "))

                    b = int(input("Enter Blue value (0-255):- "))
                    g = int(input("Enter Green value (0-255):- "))
                    r = int(input("Enter Red value (0-255):- "))

                    color = (b, g, r)

                    start_point = (x1, y1)
                    end_point = (x2, y2)

                    cv2.line(img2,start_point,end_point,color,thickness)

                cv2.imshow("Your image is:-", img2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            
            elif user_1 == "2":
                
                cir_count = int(input("How many circle do you need:-"))
                
                for i in range(cir_count):

                    print(f"\n{i+1}")
                    
                    cen_x = int(input("Enter the first number for center:-"))
                    
                    cen_y = int(input("Enter the second number for center:-"))
                    
                    center = (cen_x,cen_y)
                    
                    radius = int(input("Enter the radius:-"))
                    
                    b = int(input("Enter Blue value (0-255):- "))
                    g = int(input("Enter Green value (0-255):- "))
                    r = int(input("Enter Red value (0-255):- "))
                    
                    color = (b, g, r)
                    
                    thickness = int(input("Enter the thickness:-"))
                    
                    cv2.circle(img2,center,radius,color,thickness)
                    
                    cv2.imshow("Your image is:-", img2)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            
            elif user_1 == "3":
                
                 (h,w) = img2.shape[:2]
                 
                 center = (w//2 ,h//2)
                 
                 angle = int(input("Enter the angle:-"))
                 
                 scale = float(input("Enter the scale-"))
                 
                 M =cv2.getRotationMatrix2D(center,angle,scale)
                 
                 rotated = cv2.warpAffine(img2,M ,(w,h))
                 
                 cv2.imshow("Your image is:-", rotated)
                 cv2.waitKey(0)
                 cv2.destroyAllWindows()
            
            elif user_1 == "4":

                us_1 = int(input(
                    "Enter 1 for horizontal, "
                    "Enter 2 for vertical, "
                    "Enter -1 for both:- "
                ))

                if us_1 == 1:
                    flip_code = 1      # Horizontal

                elif us_1 == 2:
                    flip_code = 0      # Vertical

                elif us_1 == -1:
                    flip_code = -1     # Both

                else:
                    print("Invalid choice!")
                    continue

                flipped = cv2.flip(img2, flip_code)

                img2 = flipped

                cv2.imshow("Your image is:-", img2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            
            elif user_1 == "5":
                
                rect = int(input("How many rectangle you want to draw"))
                
                for i in range(rect):
                    
                    print(f"\n{i+1}")
                    
                    r1= int(input("Enter x1:-"))
                    
                    r2 = int(input("Enter y1:-"))
                    
                    r3 =int(input("Enter x2:-"))
                    
                    r4 = int(input("Enter y2:-"))
                    
                    start_point = (r1,r2)
                    
                    ending_point = (r2,r4)   
                    
                    b = int(input("Enter Blue value (0-255):- "))
                    g = int(input("Enter Green value (0-255):- "))
                    r = int(input("Enter Red value (0-255):- "))
                    
                    color = (b,g,r)
                    
                    thickness = int(input("Enter the thickness:-"))
                    
                    cv2.rectangle(img2,start_point,ending_point,color,thickness)
                    
                    cv2.imshow("Your image is:-", img2)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    
                    
            elif user_1 == "6":
                
                txt = str(input("Which text you want to write in image:-"))
                
                fontscale = int(input("Enter the scale of font:-"))
                
                b = int(input("Enter Blue value (0-255):- "))
                g = int(input("Enter Green value (0-255):- "))
                r = int(input("Enter Red value (0-255):- "))
                
                color = (b,g,r)
                
                thickness = int(input("Enter the thickness:-"))
                
                t1 =int(input("Enter x1:-"))
                
                t2 = int(input("Enter x2:-"))
                
                txt1 = (t1,t2)
                
                cv2.putText(img2,txt,txt1,cv2.FONT_HERSHEY_COMPLEX,fontscale,color,thickness)
                
                cv2.imshow("Your image is:-", img2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
            else:
                print("This option is not implemented yet.")

        elif user_0 == "exit":
            print("Program closed.")
            break

        else:
            print("Invalid input!")
            