def searchStudent(students, lastName):
    for student in students:
        if lastName == student.lastName:
            print("\nStudent: " + student.lastName + ", " +  student.firstName + 
               " GPA: " + student.GPA + 
               " Classroom: " + student.classroom + 
               " Teacher: " + student.teacherLastName + ", " + student.teacherFirstName + 
               "\n")

def searchStudentBus(students, lastName, bus):
    for student in students:
        if lastName == student.lastName:
            print("\nStudent: " + student.lastName + ", " +  student.firstName + 
               " Bus Route: " + student.bus + 
               "\n")

def searchTeacher(students, lastName):
    for student in students:
        if lastName == student.teacherLastName:
            print("\nStudent: " + student.lastName + ", " +  student.firstName + "\n")