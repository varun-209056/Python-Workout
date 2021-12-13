name = input("Student name: ")
maths = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
it = int(input("IT: "))

per = ((maths+english+science+it)/200)*100

print(f"Total Percentage scored {per}")

if per >= 65:
    print("Pass")
else:
    print("Fail")
         
