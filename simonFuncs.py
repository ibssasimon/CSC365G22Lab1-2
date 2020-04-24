from schoolsearch import populateStudents
import unittest
import sys



# Class definition for student
class Student:
    def __init__(self, lastName, firstName, grade, classroom, bus, GPA, teacherLastName, teacherFirstName):
        self.lastName = lastName
        self.firstName = firstName
        self.grade = grade
        self.classroom = classroom
        self.bus = bus
        self.GPA = GPA
        self.teacherLastName = teacherLastName
        self.teacherFirstName = teacherFirstName


class TestSimonFuncs(unittest.TestCase):
    students = populateStudents("list.txt")
    # Test case asserts return value of searching all grade 3 students, against expected output
    def test_searchGradeR7(self):
        self.assertEqual(searchGradeR7(students, 3), (["First Name: XUAN\nLast Name: COOKUS", 
            "First Name: SHANTE\nLast Name: ELHADDAD",
            "First Name: HYE\nLast Name: BRODERSEN",
            "First Name: SHARRI\nLast Name: SWEDLUND",
            "First Name: MANIE\nLast Name: CIGANEK",
            "First Name: TOMAS\nLast Name: COVINGTON",
            "First Name: TORY\nLast Name: EARLY",
            "First Name: LELA\nLast Name: LINHART",
            "First Name: GRACE\nLast Name: THEUNISSEN"]))
        

    # Test case asserts return value of R9 against student with lowest or higheset GPA in class
    def test_searchGradeR9(self):
        self.assertEqual(searchGradeR9(students, 6, "High"), "Name: PHUONG SCHOENECKER\nGPA: 3.15\nTeacher: JAE GAMBREL\nBus: 0")


    #Test case asserts return value of R10 against students the average GPA in a grade level
    def test_searchAverageR10(self):
        self.assertEqual(searchAverageR10(students, 4), "Grade level: 4\nAverage GPA: 2.95133333333")
#R7 function takes in a number as input, and prints the student(s) first and last name with matching GPAs
def searchGradeR7(students, number):
    returnString = []
    for student in students:
        if int(student.grade) == number:
            print("First Name: " + student.firstName)
            print("Last Name: " + student.lastName)
            print("")
            studentGrade = "First Name: {}\nLast Name: {}".format(student.firstName, student.lastName)
            returnString.append(studentGrade)

    return returnString
#R9 function takes in a number and high/low. Returns student in same grade with lowest or highest GPA
def searchGradeR9(students, teachers, number, flag):
    studentsInSameGrade = []
    high = 0
    low = 0
    curr = Student("","",0,0,0,0.0,"","")
    if flag == "L" or flag == "Low":
        # 'Low' was passed in, return lowest GPA student
        low = 1

    elif flag == "H" or flag == "High":
        # 'High' was passed in, return highest GPA student
        high = 1

    #Populate students with same grade
    for student in students:
        if int(student.grade) == number:
            studentsInSameGrade.append(student)
    
    #Filter for either lowest or highest GPA
    for s in studentsInSameGrade:
        curr = studentsInSameGrade[0]
        if low == 1:
            if s.GPA < curr.GPA:
                curr = s
        elif high == 1:
            if s.GPA > curr.GPA:
                curr = s

    

    for teacher in teachers:
        if teacher.classroom == curr.classroom:
            print("Name: " + curr.firstName + " " + curr.lastName)
            print("GPA: " + str(curr.GPA))
            print("Teacher: " + teacher.firstName + " " + teacher.lastName)
            print("Bus: " + str(curr.bus))
            studentGPA = "Name: {} {}\nGPA: {}\nTeacher: {} {}\nBus: {}".format(curr.firstName, curr.lastName, curr.GPA, teacher.firstName, teacher.lastName, curr.bus)

            return studentGPA


#R10 function takes in a number and returns the average GPA of all students with matching grade
def searchAverageR10(students, number):
    studentsInSameGrade = []
    for student in students:
        if int(student.grade) == number:
            studentsInSameGrade.append(student)


    sum = 0
    ct = 0
    for student in studentsInSameGrade:
        sum += float(student.GPA)
        ct += 1

    if ct == 0:
        return
    avg = sum / ct
    avg = round(avg,2)
    print("Grade level: " + str(number))
    print("Average GPA: " + str(avg))
    avgData = "Grade level: {}\nAverage GPA: {}".format(number, avg)
    return avgData





if __name__ == "__main__":
    unittest.main()
