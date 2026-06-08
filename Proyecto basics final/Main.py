from Menu import menu

options = menu()

if options == 1:
    from Actions.option_1_Manual_entry import option_1
    Students = option_1() 

    from Data.export_csv_names_grades import export_csv
    export_csv(Students) 
    
    from Actions.Topaverages import averages_diccionary, print_averages, top_3_students
    students_average = averages_diccionary()
    print_averages()
    top_3_students()

if options == 2:
    from Actions.Option_2_infoofresgisteredstudents import open_cvs_students, show_students
    Students = open_cvs_students()
    show_students(Students)
    
    from Data.export_csv_names_grades import export_csv
    export_csv(Students) 
    
    from Actions.Topaverages import averages_diccionary, print_averages, top_3_students
    students_average = averages_diccionary()
    print_averages()
    top_3_students()
    
if options == 3:
    from Data.Import_cvs import import_students
    Students = import_students()
    
    from Data.export_csv_names_grades import export_csv
    export_csv(Students) 
    
    from Actions.Topaverages import averages_diccionary, print_averages, top_3_students
    students_average = averages_diccionary()
    print_averages()
    top_3_students()
