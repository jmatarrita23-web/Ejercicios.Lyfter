def only_letters():
    while True:
        name = input("Ingrese el nombre del estudiante: ")
        if name.replace(" ", "").isalpha():
            return name
        print("Nombre inválido")


def from_1_to_100(subject):
    while True:
        try:
            nota = int(input(f"Ingrese la nota de {subject}: "))
            if 1 <= nota <= 100:
                return nota
        except ValueError:
            pass

        print("La nota debe estar entre 1 y 100")


def int_numbers():
    while True:
        try:
            return int(input("Ingrese el número de estudiantes: "))
        except ValueError:
            print("Ingrese un número válido")

class Student:
    def __init__(self, name, section,nota_espanol, nota_ingles,nota_sociales, nota_ciencias):

        self.name = name
        self.section = section
        self.nota_espanol = nota_espanol
        self.nota_ingles = nota_ingles
        self.nota_sociales = nota_sociales
        self.nota_ciencias = nota_ciencias


def option_1():

    students = []

    cantidad = int_numbers()

    for i in range(cantidad):

        student = Student(
            only_letters(),
            input("Ingrese el grado de sección del estudiante: "),
            from_1_to_100("Español"),
            from_1_to_100("Inglés"),
            from_1_to_100("Sociales"),
            from_1_to_100("Ciencias")
        )

        students.append(student)

    return students