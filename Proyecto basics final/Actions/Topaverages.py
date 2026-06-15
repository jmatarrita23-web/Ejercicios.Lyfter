
    
def averages_diccionary(students):
    
    students_average = {}

    for student in students:
        average = (
            student["nota_espanol"] +
            student["nota_ingles"] +
            student["nota_sociales"] +
            student["nota_ciencias"]
        ) / 4

        students_average[student["name"]] = average

    return students_average

def print_average(students_average):
    
    total_average = sum(students_average.values()) / len(students_average)

    print(total_average)

def top_3_students(students_average):

    
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
            
