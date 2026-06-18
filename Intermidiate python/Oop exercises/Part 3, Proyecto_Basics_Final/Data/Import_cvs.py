import csv
from Actions.option_1_Manual_entry import Student


def import_students():
    file_path = input("Enter the CSV file path: ").strip('"')

    students = []

    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:

                student = Student(
                    row["nombre"],
                    row["section"],
                    int(row["nota_espanol"]),
                    int(row["nota_ingles"]),
                    int(row["nota_sociales"]),
                    int(row["nota_ciencias"])
                )

                students.append(student)

        print("Students imported successfully.")
        return students

    except FileNotFoundError:
        print("No se encontró el archivo.")
        return []