"""
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
"""
def gradingStudents(grades):
	roundGrades =[]
	for i in range(len(grades)):
		if grades[i] < 38:
			roundGrades.append(grades[i])
		else:
			multi_5 = (grades[i] - (grades[i] % 5)) + 5			
			if multi_5 - grades[i] < 3:
				roundGrades.append(multi_5)
			else:
				roundGrades.append(grades[i])
	return roundGrades

if __name__ == "__main__":
	grades =  [73,67,38,33]
	print gradingStudents(grades)