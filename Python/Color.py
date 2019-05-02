color1 = input("Choose 1st color (Red,Blue,Yellow):")
color2 =input("Choose 2nd color (Red,Blue,Yellow):")

if (color1 == 'Red' and color2 == 'Blue'):
    print("The color is Purple")
elif(color1 == 'Red' and color2 == 'Yellow'):
    print("The color is Orange")
elif(color1 == 'Blue' and color2 == 'Yellow'):
    print("The color is Green")
else:
    print("Please choose only from the given three color options!!")

