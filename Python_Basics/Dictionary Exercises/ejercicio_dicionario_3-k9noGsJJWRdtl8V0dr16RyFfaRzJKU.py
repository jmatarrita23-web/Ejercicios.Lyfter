profile = ["name", "age", "occupation"]
answers = ["Marcos", 30, "Engineer"]

my_diccionary = {}

for i in range(len(profile)):
    my_diccionary[profile[i]] = answers[i]

print(my_diccionary)

keys_to_delete = ['name', 'age', 'occupation']
response = input("Do you want to erase the dictionary? (yes/no): ")
if response.lower() == "yes":
    for key in keys_to_delete:
        my_diccionary.pop(key, None)
    print ("Dictionary erased.")
else:
    print("Dictionary not erased.")
print("Final:", my_diccionary)