def flip(text):
    reversed_text = ""

    for i in range(len(text)-1, -1, -1):
        reversed_text += text[i]

    return reversed_text
text= input("ingresa un texto: ")
print(flip(text))