# importing the arguement variable
from sys import argv
# attaching variables to the arguments from when you launched
script, filename = argv

# printing the filename to be used
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# creating a variable that refers to the opened file
print "Opening the file..."
target = open(filename, 'w')

# truncates the file for some reason, not sure why
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# just asks for three things that will be added to the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# writes out to the file with a return statement as well 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# and you always close the file
print "And finally, we close it."
target.close()




