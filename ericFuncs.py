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

def searchTeachersOfGrade(teachers, grade):
    for teacher in teachers:
        if teacher.grade == grade:
            print(" Teacher: " + teacher.lastName + ", " + teacher.firstName + "\n")

def searchTeacherFactor(students, teachers, lastName):
    numStudents = 0
    classroom = 0
    totalGPA = 0
    averageGPA = 0
    for teacher in teachers:
        if teacher.lastName == lastName:
            classroom = teacher.classroom
            for student in students:
                if student.classroom == classroom:
                    numStudents += 1
                    totalGPA += student.GPA
            averageGPA = round((totalGPA / numStudents), 2)
            print(teacher.lastName + ", " + teacher.firstName + " has " + numStudents + 
                " in classroom " + classroom + " with an average GPA of " + averageGPA + "\n")