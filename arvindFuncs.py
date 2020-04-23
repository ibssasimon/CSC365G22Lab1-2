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

    
