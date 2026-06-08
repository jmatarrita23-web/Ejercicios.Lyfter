from Actions.Option_2_infoofresgisteredstudents import open_cvs_students
    
def averages_diccionary():
    students_average = {}
    students = open_cvs_students()
    for name, grade in students.items():
        average = (
            grade["nota_espanol"] +
            grade["nota_ingles"] +
            grade["nota_sociales"] +
            grade["nota_ciencias"]
        ) / 4
        students_average[name] = average
    return students_average
students_average = averages_diccionary()

def print_averages():
    for name, average in students_average.items():
        print(f"{name}: {average}")

def top_3_students():

    
    first_place = 0

    for average in students_average.values():
        if average > first_place:
            first_place = average

    for name, average in students_average.items():
        if average == first_place:
            print(f"Primer lugar: {name} con un promedio de {average}")
            
    second_place = 0
    for average in students_average.values():
        if average > second_place and average < first_place:
            second_place = average
            
    for name, average in students_average.items():
        if average == second_place:
            print(f"Segundo lugar: {name} con un promedio de {average}")
            
    third_place = 0
    for average in students_average.values():
        if average > third_place and average < second_place:
            third_place = average

    for name, average in students_average.items():
        if average == third_place:
            print(f"Tercer lugar: {name} con un promedio de {average}")
            
