total_grades = int(input("Ingrese la cantidad total de notas: "))
passed_grades_count = 0
failed_grades_count = 0
passed_grades_average = 0
failed_grades_average = 0
overall_average = 0
grades_counter = 1
Total_sum_grades = 0
while grades_counter <= total_grades:
    grade = int(input("Ingrese la nota numero:"))
    grades_counter = int(grades_counter) + 1
    Total_sum_grades = Total_sum_grades + grade
    print(grades_counter)
    if grade >= 70:
        passed_grades_count = int(passed_grades_count + 1)
        passed_grades_average = passed_grades_average + grade
    else:
        failed_grades_count = int(failed_grades_count + 1)
        failed_grades_average = failed_grades_average + grade
if passed_grades_count == 0:
        passed_grades_average = 0
else:
    passed_grades_average = passed_grades_average / passed_grades_count
if failed_grades_count == 0:
        failed_grades_average = 0
else:
    failed_grades_average = failed_grades_average / failed_grades_count

overall_average = Total_sum_grades / total_grades
print("El estudiante tiene esta cantidad de notas aprobadas", passed_grades_count)
print("El promedio de notas aprobadas es:", passed_grades_average)
print("El estudiante tiene esta cantidad de notas desaprobadas", failed_grades_count)
print("El promedio de notas desaprobadas es:", failed_grades_average)
print("El promedio de notas total es:", overall_average)

