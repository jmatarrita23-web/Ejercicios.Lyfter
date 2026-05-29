number = []

for i in range(10):
    num = int(input(f"Ingrese el número {i}: "))
    number.append(num)
mayor = max(number)

print("Lista de números:", number )
print("El número más alto fue:", mayor)