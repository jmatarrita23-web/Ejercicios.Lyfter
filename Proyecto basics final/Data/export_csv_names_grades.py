import csv

def export_csv(students):
    rute = "estudiantes.csv"

    with open(rute, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "nombre",
            "section",
            "nota_espanol",
            "nota_ingles",
            "nota_sociales",
            "nota_ciencias"
        ])

        for student in students:
            writer.writerow([
                student["name"],
                student["section"],
                student["nota_espanol"],
                student["nota_ingles"],
                student["nota_sociales"],
                student["nota_ciencias"]
            ])

    print(f"Archivo '{rute}' exportado exitosamente.")