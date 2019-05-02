age = int(input("Enter your age: "));

if(age <= 1):
    print("You are infant")
elif(age >1 and age<13):
    print("You are a child")
elif(age >13 and age<20):
    print("You are a Teenager")
elif(age >=20 and age<=110):
    print("You are an adult!!")
else:
    print("Enter valid input")
