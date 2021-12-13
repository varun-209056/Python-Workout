amount = int(input("Enter the amount of the product: "))

if amount < 1000:
    discount1 = (amount)*(5/100)
    payment =  amount - discount1
    print(f"Discount on the product: {discount1}")
    print(f"The Net payable amount is : {payment}")

elif amount > 4000 and amount < 5000:
    discount2 = (amount)*(10/100)
    payment =  amount - discount2
    print(f"Discount on the product: {discount2}")
    print(f"The Net payable amount is: {payment}")
else:
    print(f"No discount is available on this amount: {amount}")
    print(f"Net payable amount: {amount}")
    
