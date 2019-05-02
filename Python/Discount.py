userPackages = int(input("Enter the number of packages bought: "))

packagePrice = 99

if (userPackages < 10):
    discount = 0
elif (userPackages < 20):
    discount = 0.10
elif (userPackages < 50):
    discount = 0.20
elif (userPackages < 100):
    discount = 0.30
else:
    discount = 0.40

totalPrice = userPackages * packagePrice
totalDiscountAmt = discount * totalPrice
grandTotal = totalPrice - totalDiscountAmt

print("Discount Amount: " + str(totalDiscountAmt))
print("Your total amount to pay: " + str(grandTotal))
