def only_letters():
    while True:
        name = input("Ingrese el nombre del estudiante: ")
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Por favor, ingrese un nombre válido que contenga solo letras y espacios.")

def from_1_to_100(subject):
    while True:
        try:
            nota = int(input(f"Ingrese la nota de {subject} entre 1 y 100: "))
            if 1 <= nota <= 100:
                return nota 
            else:                print("La nota debe estar entre 1 y 100. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido del 1 al 100.")
            continue

def int_numbers():
    while True:
        try:
            number_students = int(input("Ingrese el número de estudiantes: "))
            return number_students
        except ValueError:
            print("Por favor, ingrese un número válido.")

def option_1():
    
    number_students = int_numbers()
    Students={}
    
    for i in range(number_students):
        
        name = only_letters()

        Students[name] = {
            "section": input("Ingrese el grado de sección  del estudiante: "),
            "nota_espanol": from_1_to_100("Español"),
            "nota_ingles": from_1_to_100("Inglés"),
            "nota_sociales": from_1_to_100("Sociales"),
            "nota_ciencias": from_1_to_100("Ciencias")
        }

    print (Students)
    return Students

