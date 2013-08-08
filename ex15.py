# from the sys module we are importing the argv function
from sys import argv

# we are giving it two arguments, you type this in when you run
# the program from a prompt.you are really only adding the filename at the end.
script, filename = argv


# creates a variable txt that refers to the opened file from the argu. 
txt = open(filename)

# prints out the argument for the filename we used when launching the script
print "Here's your file %r:" % filename
# the variable uses a built in function to read the txt file we are referring to
# and prints out all the contents for us
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

