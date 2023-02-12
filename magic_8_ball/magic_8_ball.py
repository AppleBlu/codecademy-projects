# importing modules
import random

# declairing variables
name = 'Negitive'
question = 'Is this magic?'
awnser = ''
random_number = random.randint(1, 9)

# prints random_number to test that it is random
#print(random_number)

# creating an if statement to give the awnsers
if random_number == 1:
  awnser = 'Yes, definitly.'
elif random_number == 2:
  awnser = 'It is decidedly so.'
elif random_number == 3:
  awnser = 'Without a doubt.'
elif random_number == 4:
  awnser = 'Reply hazy, try again.'
elif random_number == 5:
  awnser = 'Ask again later.'
elif random_number == 6:
  awnser = 'Better not tell you now.'
elif random_number == 7:
  awnser = 'My sources say no.'
elif random_number == 8:
  awnser = 'Outlook not so good.'
elif random_number == 9:
  awnser = 'Very doubtful.'
else:
  awnser = 'Error'

# printing the display
if len(question) == 0:
  print('Please enter a question')
elif len(question) > 0 and len(name) == 0:
  print(question)
  print('''The magic 8-ball's awnser is: ''' + awnser)
else: 
  print(name + ' asked: ' + question)
  print('''The magic 8-ball's awnser is: ''' + awnser);