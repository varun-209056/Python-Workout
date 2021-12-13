
print("Select whose area you want to find: ")
print("1.Circle")
print("2.Square")
print("3.Rectangle")
#print("4.Exit")

count = int(input("How many times do you want to run the program: "))
i = 0
#for i in range(0,count):
while (i<count):
            opt = int(input("Select an option 1,2,3: "))
            if opt == 1:

                r = int(input("Enter the radius: "))
                area_circle = 3.14*(r**2)
                print(f"Area of the Circle is: {area_circle}")

            elif opt == 2:

                a = int(input("Enter the side of the square: "))
                area_sq = a**2
                print(f"Area of the Square is: {area_sq}")

            elif opt == 3:

                l = int(input("Length of the Rectangle: "))
                b = int(input("Breadth of the Rectangle: "))
                area_rect = l*b
                print(f"Area of the Rectangle: {area_rect}")

            
            
            else:
                print("Invalid Input")
            i+=1
            
    
