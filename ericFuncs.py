def searchStudent(students, teachers, lastName):
    for student in students:
        if lastName == student.lastName:

            for teacher in teachers:
                if teacher.classroom == student.classroom:
                    print("\nStudent: " + student.lastName + ", " +  student.firstName + 
                    " GPA: " + student.GPA + 
                    " Classroom: " + student.classroom + 
                    " Teacher: " + teacher.lastName + ", " + teacher.firstName + 
                    "\n")
           

def searchStudentBus(students, lastName, bus):
    if bus == "B" or bus == "Bus":
        for student in students:
            if lastName == student.lastName:
                print("\nStudent: " + student.lastName + ", " +  student.firstName + 
                " Bus Route: " + student.bus + 
                "\n")
    

def searchTeacher(students, teachers, lastName):
    for teacher in teachers:
        if lastName == teacher.lastName:
            classroom = teacher.classroom

            for student in students:
                if student.classroom == classroom:
                    print("\nStudent: " + student.lastName + ", " +  student.firstName + "\n")