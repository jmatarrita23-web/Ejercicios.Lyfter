import csv
def export_csv(students):
    rute = "estudiantes.csv"
    with open (rute, mode="w",newline="") as file:
        escritor = csv.writer(file)
        
        for student in students:
            escritor.writerow([
                student["name"],
                student["section"],
                student["nota_espanol"],
                student["nota_ingles"],
                student["nota_sociales"],
                student["nota_ciencias"]
            ])
    print(f"Archivo '{rute}' exportado exitosamente.")