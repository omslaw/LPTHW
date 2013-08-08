# imports the argv variable from sys
from sys import argv

# attaching the variables to the argv variables
script, filename = argv

# just printing some warning lines about what is going to happen
print "So let's create a new file from scratch."
print "Make sure you have deleted the file first before running this script."
print "If not might as well hit CTRL-C (^C) now."

raw_input("Hit enter to continue")

# opens or creates the file if it doesn't exist
target = open(filename, 'w')

print "Now type in the lines you want to add to the file"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "\nWriting them to %r now" % filename

returnKey = "\n"

# writes out the inputes and seperates it with a new line
target.write({line1, line2})  

print "\nNow we are closing %r." % filename
target.close()
print "\nNow lets attempt to open/read %r." % filename

target_again = open(filename)
print "Here are the items you added to %r: " % filename
print "\n"
target_again.read()


