profile = ["name", "age", "occupation"]
answers = ["Marcos", 30, "Engineer"]

my_diccionary = {}

for i in range(len(profile)):
    my_diccionary[profile[i]] = answers[i]

print(my_diccionary)