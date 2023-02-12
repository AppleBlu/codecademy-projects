from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Creating a list to hold the stacks
stacks = []

# Initializing 3 Stacks with Left, Middle and Right values
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')

# Adding all the stacks to the stacks[] list
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Setting up the Game
# Getting the user to input how many disks they want to play with
num_disks = int(input('\nHow many disks do you want to play with?\n'))

# Checking that the user entered a number greater than three
while num_disks < 3:
    num_disks = int(input('Enter a number greater than or equal to 3\n'))

# Iterating backwards through  the range of num_of_disks and pushes it onto the first stack (left stack)
# For example: if user picks 3 then this would return 3 then 2 then 1. Adding each to left stack with 3 being the tail
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

# This will tell the user how quick they can complete the puzzle in moves dependent on how many disks they picked to
# play with
num_optimal_moves = 2 ** num_disks - 1
print(f'\nThe fastest you can solve this game is in {num_optimal_moves} moves')


# Getting the User's Inputs
# Setting the variable choices to equal the first letter of each stack name
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]

    # Creating a while loop to make sure the user enters a valid stack
    while True:

        # Creating a for loop to display each stack with the corresponding letter input

        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f'Enter {letter} for {name}')
        user_input = input('')

        # Checking that the user input is in choices
        if user_input in choices:

            # Returning the stack the user selected
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


# Playing the Game
# setting the number of moves the user has made to 0
num_user_moves = 0

# Creating a while loop to check the user has not completed the puzzle yet
while right_stack.get_size() != num_disks:

    # If the while loop is true the current stacks get printed
    print('\n\n\n...Current Stacks...')
    for i in stacks:
        i.print_items()

    # Creating a while loop to print the stacks you can move from and move to including the users inputs
    while True:
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()
        print('\nWhich stack do you want to move to?\n')
        to_stack = get_input()

        # Using an if statement to check the user is not trying to move from an empty stack
        if from_stack.is_empty():
            print('\n\nInvalid Move. Try Again')

        # Using an elif statement to push onto the next stack if requirements are met
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            # Increasing the users moves to display at the end
            num_user_moves += 1
            break
        else:
            print('\n\nInvalid Move. Try Again')

# Once the user completes the puzzle this will be printed
print(f'\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}')
