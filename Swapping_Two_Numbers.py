num1 = int(input("Enter first Value:"))
num2 = int(input("Enter second Value:"))
'''
c = num2
num2 = num1
num1 = c
'''
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

num1,num2 = num2,num1

print("num1=",num1)
print("num2=",num2)





