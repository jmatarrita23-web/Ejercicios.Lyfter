Number1 = int(input("Enter the first number: "))

Number2 = int(input("Enter the second number: "))

Number3 = int(input("Enter the third number: "))

if Number1 > Number2 and Number1 > Number3:
    print("The largest number is: ", Number1)
elif Number2 > Number1 and Number2 > Number3:
    print("The largest number is: ", Number2)
else:
    print("The largest number is: ", Number3)