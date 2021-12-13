n = input("Enter any input: ")

if n>="0" and n<="9"  :
    print(f"{n} is an integer")

elif n>="a" and n<="z":
    print(f"{n} is a small alphabet")

elif n>="A" and n<="Z":
    print(f"{n} is a capital alphabet")

else:
    print(f"{n} is a special character")

