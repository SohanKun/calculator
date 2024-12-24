print('     SIMPLE CALCULATOR       ')
num1=float(input("Enter first number : "))  #taking first number input from user
num2=float(input("Enter second number : "))  #taking second number input from user
choice=0
while choice<=5:
    print("press 1 for ADDITION \npress 2 for SUBTRACTION \npress 3 for MULTIPLICATION \npress 4 for DIVISION \npress 5 for POWER")
    choice=int(input("Enter your choice from 1 to 4 : "))  #taking input from user
    if choice==1:
        print("The addition of given two numbers is : ",num1+num2)  #addition of two numbers
    elif choice==2:
        print("The subtraction of given two numbers is : ",num1-num2)  #subtraction of two numbers
    elif choice==3:
        print("The multiplication of given two numbers is : ",num1*num2)  #amultiplication of two number
    elif choice==4:
        print("The division of given two numbers is : ",num1/num2)  #division of two numbers
    elif choice==5:
        print("The power is : ",num1**num2)  #power of two numbers
    else:
        print("Invalid choice")