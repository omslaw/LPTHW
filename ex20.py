# importing the argument statement since we will be using it
from sys import argv

# creating the variables that will be used for the argv import
script, input_file = argv

# creating a function that prints the entire contents of a file
def print_all(f):
    # the actual statement that prints the file to screen
    print f.read()

# creating a function that rewinds the file since otherwise it would be blank
def rewind(f):
    # the actual command seek that rewinds the file back to the beginning since it's 0
    f.seek(0)

# function that will will use two variables, one will be for the actual line number
def print_a_line(line_count, f):
    # print statement using the line number to read and the command for the reading a line
    print line_count, f.readline()

# now create a variable that refers to the file we are opening
current_file = open(input_file)

# basic print statement
print "First let's print the whole file:\n"

# calls function using the name we typed in when launching python. 
print_all(current_file)

# basic print statement about what are about to do 
print "Now let's rewind, kind of like a tape."

# calls the rewind function to rewind the file that we just read
rewind(current_file)

# basic print statement about what we are going to do
print "Let's print three lines:"

# creating a variable that will refer to an number that will be used for reading 
# each specific line
current_line = 1
# calls the function that reads back line by line. starting from the variable we just gave it
# and of course you need the filename as well thus two variable for the function
print_a_line(current_line, current_file)

# just adds one to the previously used variable so it reads the next line
# the number is now number 2
current_line += 1
# calling the function again, and should now read the next line
print_a_line(current_line, current_file)

# same as the previous two commands, just adds one to variable and reads the next line in the file
# the number for the variable is now 3
current_line += 1
print_a_line(current_line, current_file)

