def open_cvs_students():
    import csv
    Students = {}
    with open("estudiantes.csv", mode="r") as file:
        lector = csv.reader(file)
        
        for row in lector:
            name = row[0]
            grade = {
                "section": row[1],
                "nota_espanol": int(row[2]),
                "nota_ingles": int(row[3]),
                "nota_sociales": int(row[4]),
                "nota_ciencias": int(row[5])
            }
            Students[name] = grade
    
    return Students

def show_students(Students):
    
    print(Students)



            