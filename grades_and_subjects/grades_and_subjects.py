#values for last years subjects and grades
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#values for subjects
subjects = ['physics', 'calculus', 'poetry', 'history']

#adds computer science to subjects  
subjects.append('computer science')

#values for grades
grades = [98, 97, 85, 88]

#add 100 to grades
grades.append(100)

#adds grades and subjects to a vairible called gradebook
gradebook = list(zip(grades, subjects))

#adds visual arts and its grade to gradebook
gradebook.append(("visual arts", 93))

#prints this sentence
print('This years grades!')

#prints gradebook
print(list(gradebook))

#making a gap
print(' ')
print(' ')
print(' ')
print(' ')

#prints this sentence
print('This year and last years grades!')

#adds last years and this years grades to full gradebook
full_gradebook = gradebook + last_semester_gradebook

#prints full gradebook
print(list(full_gradebook))