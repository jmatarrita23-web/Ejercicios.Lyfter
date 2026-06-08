name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

print(f"Hello {name} {last_name}, you are {age} years old.")
if int(age) < 2:
    print("You are a baby.")
if int(age) > 2 and int(age) < 10:
    print("You are a child.")
if int(age) > 10 and int(age) < 12:
    print("You are a pre-teen.")
if int(age) > 12 and int(age) < 18:
    print("You are a teenager.")
if int(age) > 18 and int(age) < 29:
    print("You are a young adult.")
if int(age) > 29 and int(age) < 59:
    print("You are an adult.")
if int(age) > 59:
    print("You are a senior.")