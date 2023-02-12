#random test
def greater_than(x, y):
  if x > y:
    return x
  if y > x:
    return y
  if y == x:
    return 'These numbers are the same'
  
print(greater_than(-5, -5))

#if you get in or not
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."
  
print(graduation_reqs(2.0, 120))

#grading sytem in letters
def grade_converter(gpa):
  if gpa >= 4.0:
    return 'A'
  elif gpa >= 3.0:
    return 'B'
  elif gpa >= 2.0:
    return 'C'
  elif gpa >= 1.0:
    return 'D'
  else: 
    return 'F'
grade = grade_converter(2.3)
print('Your grade is ' + grade + '!')

#if applicants should be viewed for the college
def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return 'This applicant should be accepted.'
  elif (gpa >= 3.0) and (ps_score >= 90):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."
print(applicant_selector(3.0, 120, 120))