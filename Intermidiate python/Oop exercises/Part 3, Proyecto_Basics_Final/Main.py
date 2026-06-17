from Menu import menu

students=[]

while True:
    
    
    options = menu()

    if options == 1:
        from Actions.option_1_Manual_entry import option_1
        new_students = option_1()
        students.extend(new_students)

    if options == 2:
        for student in students:
            print(student.name)
            print(student.section)
            print(student.nota_espanol)
            print(student.nota_ingles)
            print(student.nota_sociales)
            print(student.nota_ciencias)
        
    if options == 3:
        
        from Actions.Topaverages import averages_diccionary, top_3_students
        students_average = averages_diccionary(students)
        top_3_students(students_average)
    
    if options == 4:
        from Actions.Topaverages import averages_diccionary, print_average
        students_average = averages_diccionary(students)
        print_average(students_average)
        
    if options == 5:
        from Data.export_csv_names_grades import export_csv
        export_csv(students)
        
    if options == 6:
        from Data.Import_cvs import import_students
        students=import_students()
        
        
    if options == 7:
        print ("end")
        break