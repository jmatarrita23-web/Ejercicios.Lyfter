def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. borrar resultado")

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def get_choice():
    while True:
        try:
            choice = int(input("Seleccione una opción: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            
def operation(actual_result, choice, num):

    if choice == 1:
        return actual_result + num

    elif choice == 2:
        return actual_result - num

    elif choice == 3:
        return actual_result * num

    elif choice == 4:
        if num == 0:
            print("Error: No se puede dividir por cero.")
            return actual_result

        return actual_result / num

def calculator():

    actual_result = get_number("Ingrese el un numero para empezar: ")
    while True:
        menu()
        
        choice = get_choice()

        if choice == 5:
            actual_result = 0
            

        num = get_number("Ingrese un número: ")

        actual_result = operation(actual_result, choice, num)

        print(actual_result)
        continue
calculator()