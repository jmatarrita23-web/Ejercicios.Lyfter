def menu_option():
    while True:
        try:
            option = int(input("Ingrese una opción: "))

            if 1 <= option <= 6:
                return option
            else:
                print("Seleccione una opción entre 1 y 6.")

        except ValueError:
            print("Por favor, ingrese un número válido.")


def menu():
    print("Bienvenido al menú de opciones")
    print("1. Ingresar informacion de estudiantes")
    print("2. Ver la informacion de estudiantes ingresados")
    print("3. Importar los datos de un archivo CSV")

    option = menu_option()
    return option

