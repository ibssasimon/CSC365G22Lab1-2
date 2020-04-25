from arvindFuncs import *
from simonFuncs import *
from ericFuncs import *

# Class definition for student
class Student:
    def __init__(self, lastName, firstName, grade, classroom, bus, GPA):
        self.lastName = lastName
        self.firstName = firstName
        self.grade = grade
        self.classroom = classroom
        self.bus = bus
        self.GPA = GPA
 
class Teacher:
    def __init__(self, lastName, firstName, classroom):
        self.lastName = lastName
        self.firstName = firstName
        self.classroom = classroom


def main():
    #Populate data from text file
    students = populateStudents("list.txt")
    teachers = populateTeachers("teachers.txt")
    

    # Ask for user input until user quits
    while(1):
        
        # Write the prompts for user input
        writePrompts()

        args = input("Command: ").split()
        userInput = args[0]


        ## Changes: Students and teachers are now separate entities
        # Any queries regarding student info lastName.....GPA is fine
        # Any queries regarding teacher info lastName ... classroom must be implemented to receive teachers list

        if(userInput == "Q" or userInput == "Quit"):
            break

        elif userInput == "S:" or userInput == "Student:":
            if(len(args) == 2):
                # 1 additional argument passed in
                searchStudent(students, teachers, args[1])
            elif(len(args) == 3):
                # 2 addtional arguments passed in
                # Might have to parse for "B" in bus
                # Arg 1 is "S", Arg 2 is <lastname>, Arg 3 is "B"
                searchStudentBus(students, args[1], args[2])
            else:
                print("Bad command")

        
        elif userInput == "T:" or userInput == "Teacher:":
            searchTeacher(students, teachers,  args[1])
        elif userInput == "G:" or userInput == "Grade:":
            if len(args) == 2:
                searchGradeR7(students, int(args[1]))
            else:
                searchGradeR9(students, teachers, int(args[1]), args[2])

        elif userInput == "B:" or userInput == "Bus:":
            if len(args) == 2:
                searchBus(students, args[1])
            else:
                print("Incorrect use of command")

        elif userInput == "A:" or userInput == "Average:":
            searchAverageR10(students, int(args[1]))

        elif userInput == "I" or userInput == "Info":
            searchInfo(students)
        elif userInput == "gradeFactor:" or userInput == "gF":
            pass
        elif userInput == "busFactor:" or userInput == "bF:":
            pass
        elif userInput == "teacherFactor:" or userInput == "tF:":
            pass
        else:
            print("Bad command")
            continue

        



def populateStudents(fileName1):
    #Open the file
    try:
        f1 = open(fileName1, "r")

    except FileNotFoundError:
        exit()
    
    lines1 = f1.readlines()
    students = []


    for studentLine in lines1:
        studentRawData = studentLine.strip() 
        studentInfo = studentRawData.split(",")
        try:
            lastName = studentInfo[0].strip()
            firstName = studentInfo[1].strip()
            grade = studentInfo[2].strip()
            classroom = studentInfo[3].strip()
            bus = studentInfo[4].strip()
            GPA = studentInfo[5].strip()
            
            myStudent = Student(lastName, firstName, grade, classroom, bus, GPA)
            students.append(myStudent)
        except:
            exit()
    return students

def populateTeachers(fileName2):
    #Open the file
    try:
        f2 = open(fileName2, "r")

    except FileNotFoundError:
        exit()
    
    lines = f2.readlines()
    teachers = []


    for teacherLine in lines:
        teacherRawData = teacherLine.strip() 
        teacherInfo = teacherRawData.split(", ")

        try:
            lastName = teacherInfo[0].strip()
            firstName = teacherInfo[1].strip()
            classroom = teacherInfo[2].strip()
            
            myTeacher = Teacher(lastName, firstName, classroom)
            teachers.append(myTeacher)
        except:
            exit()
    return teachers



def writePrompts():
    print("\nS[tudent]: <lastname> [B[us]]")
    print("T[eacher]: <lastname>")
    print("B[us]: <number>")
    print("G[rade]: <number> [H[igh]|L[ow]]")
    print("A[verage]: <number>")
    print("I[nfo]")
    print("Q[uit]\n")


if __name__ == "__main__":
    main()