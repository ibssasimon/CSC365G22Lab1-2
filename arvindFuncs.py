def searchInfo(students):
	# List to keep track of student grades. Each index keeps track of that index grade (Ex index 0 keeps track of grade 0)
	grades = [0] * 7
	
	# Iterating through all students
	for student in students:
		
		# Check if grade is correct type; skip student if otherwise
		try:
			grade = int(student.grade)
		except ValueError:
			print("Invalid grade type")
			continue

		# Check if grade between 0 and 6; skip student if otherwise
		if 0 <= grade <= 6:
			grades[grade] += 1
		else:
			print("Student not in grades 0-6")
			continue

	# Print values in list
	for i in range(0, 7):
		print(str(i) +  ": " + str(grades[i]))


def searchBus(students, bus):
	# Iterating through all students
	for student in students:
		
		# If bus number matches
		if bus == student.bus:
			print("\nStudent Name: " + student.firstName + " " + student.lastName)
			print("Student Grade: " + student.grade)
			print("Student Classroom: " + student.classroom)	


def reportEnrollment(students):
	enroll = {}

	for student in students:
		if student.classroom in enroll:
			enroll[student.classroom] += 1
		else:
			enroll[student.classroom] = 1

	for key in sorted(enroll.keys()):
		print(str(key) + ": " + str(enroll[key]))

def gradeFactorsGPA(students, grade):
	totalGPA = 0
	totalStudents = 0

	for student in students:
		if student.grade == grade:
			totalGPA += float(student.GPA)
			totalStudents += 1

	if totalStudents == 0:
		print("No students in this grade!")
	else:
		averageGPA = round(totalGPA / totalStudents, 3)
		print("Average GPA for grade " + grade + " is " + str(averageGPA))


def gradeFactorsBus(students, grade):
	routes = {}

	for student in students:
		if student.grade == grade:
			if student.bus in routes:
				routes[student.bus] += 1
			else:
				routes[student.bus] = 1

	print("Bus routes and number of students who take them in grade " + str(grade))

	for key in sorted(routes.keys()):
		print(str(key) + ": " + str(routes[key]))

def gradeFactorsTeacher(students, teachers, grade):
	classroom = {}

	for student in students:
		if student.grade == grade:
			if student.classroom in classroom:
				classroom[student.classroom] += 1
			else:
				classroom[student.classroom] = 1

	for key in classroom.keys():
		for teacher in teachers:
			if key == teacher.classroom:
				print("Teacher " + teacher.firstName + " " + teacher.lastName + " has " + str(classroom[key]) + " grade " + grade + " students")