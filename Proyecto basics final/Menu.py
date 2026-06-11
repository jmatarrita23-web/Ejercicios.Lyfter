def menu_option():
    while True:
        try:
            option = int(input("Ingrese una opción: "))

            if 1 <= option <= 7:
                return option
            else:
                print("Seleccione una opción entre 1 y 7.")

        except ValueError:
            print("Por favor, ingrese un número válido.")


def menu():
    
    print("Bienvenido al menú de opciones")
    print("1. Ingresar informacion de estudiantes")
    print("2. Ver la informacion de estudiantes ingresados")
    print("3. Ver top 3 estudiantes")
    print("4. Ver promedio general de los estudiantes")
    print("5. Exportar los datos a un archivo CSV")
    print("6. Importar los datos de un archivo CSV")
    print("7. Salir")
        

    option = menu_option()
    return option

