import csv
def export_csv(Students):
    rute = "estudiantes.csv"
    with open (rute, mode="a",newline="") as file:
        escritor = csv.writer(file)
        
        for nombre, notas in Students.items():
            escritor.writerow([
                nombre,
                notas ["section"], 
                notas["nota_espanol"], 
                notas["nota_ingles"], 
                notas["nota_sociales"], 
                notas["nota_ciencias"]
                ])
            
            