choice1 = "Joe's Gourmet Burgers"
choice2 = "Main Street Pizza Company"
choice3 = "Corner Cafe"
choice4 = "Mama's fine Italian"
choice5 = "The Chef's Kitchen"

vegetarian = input("Is any one in the party is vegetarian?(Yes/No)")
vegan = input("Is any one in the party is vegan?(yes/no)")
gluten_free = input("Is any one in the party is Glutan free?(Yes/No)")

if (vegetarian == 'Yes' and vegan == 'Yes' and gluten_free == 'Yes'):
    print("Here are your restaurant choices:")
    print(choice3 +'\n' + choice5 )
    
elif (vegetarian == 'Yes' and vegan == 'Yes' and gluten_free == 'No'):
    print("Here are your restaurant choices:")
    print(choice3 + '\n' + choice5 )
    
elif (vegetarian == 'Yes' and vegan == 'No' and gluten_free == 'Yes'):
    print("Here are your restaurant choices:")
    print(choice2 + '\n' + choice3 + '\n' + choice5 )
    
elif (vegetarian == 'No' and vegan == 'Yes' and gluten_free == 'Yes'):
    print("Here are your restaurant choices:")
    print(choice3 + '\n' + choice5 )
    
elif (vegetarian == 'No' and vegan == 'Yes' and gluten_free == 'No'):
    print("Here are your restaurant choices:")
    print(choice3 + '\n' + choice5 )
    
elif (vegetarian == 'No' and vegan == 'No' and gluten_free == 'Yes'):
    print("Here are your restaurant choices:")
    print(choice2 + '\n' + choice3 + '\n' + choice5 )
    
elif (vegetarian == 'Yes' and vegan == 'No' and gluten_free == 'No'):
    print("Here are your restaurant choices:")
    print(choice2 + '\n' + choice3 + '\n' + choice4 + '\n' + choice5 )
    
elif (vegetarian == 'No' and vegan == 'No' and gluten_free == 'No'):
    print("Here are your restaurant choices:")
    print(choice1 + '\n' + choice2 + '\n' + choice3 + '\n' + choice4 + '\n' + choice5 )
    
else:
    print("Enter valid choice")
    
