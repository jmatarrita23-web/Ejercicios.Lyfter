def lower_cap_letters():
    text = input("Ingrese un texto: ")
    Cap_letters = 0
    Lower_letters = 0
    for letter in text:
        if letter.isupper():
            Cap_letters = Cap_letters + 1
            
        elif letter.islower():
            Lower_letters = Lower_letters + 1
            
    print(f"El número de letras mayúsculas es: {Cap_letters}")
    print(f"El número de letras minúsculas es: {Lower_letters}")
lower_cap_letters()