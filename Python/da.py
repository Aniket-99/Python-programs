choice = 'y'
while choice == 'y':
        num = int(input("Enter a number in the range of 1 to 7:"))
        
       
        if (num == 1):
                print("Monday")
                break
        elif (num == 2):
                print("Tuesday")
                
        elif (num == 3):
                print("Wednesday")
                
        elif (num == 4):
                print("Thursday")
                
        elif (num == 5):
                print("Friday")
                
        elif (num == 6):
                print("Saturday")
               
        elif (num == 7):
                print("Sunday")
                
        else:
                print("Please enter a valid input!!")
                continue
