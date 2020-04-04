names =  input("Enter names separated by commas :").title().split(",") # get and process input for a list of names
assignments = input("Enter missed assignments separated by commas :").split(",") # get and process input for a list of the number of assignments
grades =  input("Enter grades separated by commas :").split(",") # get and process input for a list of grades
pot_grades = 100, 100, 100 # potential grades after submission

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for names, assignments, grades, pot_grades in zip(names, assignments, grades, pot_grades) :
    print(message.format(names, assignments, grades, int(grades) + int(assignments)))