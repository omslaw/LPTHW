# a variable stating there are 10 types of people
x = "There are %d types of people." % 10
# varialbe for the word binary using the same name
binary = "binary"
# another varialble like the above
do_not = "don't"
# varialbe for the whole saying
y = "Those who know %s and those who %s." % (binary, do_not)
# next two lines prints out two of the variables we created above. 
print x
print y
# prints the varialble x with ' around the quotes
print "I said: %r." % x
# prints the varialbe with the ' already printed so it looks like the %r version
print "I also said: '%s'." % y
# establishing another variable
hilarious = False
# and another one with a built in %r
joke_evaluation = "Isn't that joke so funny?! %r"
# prints out the two variables we just created in combined print statement
print joke_evaluation % hilarious
# creating another two variables
w = "This is the left side of..."
e = "a string with a right side."
# prints both variables to look like one long sentance.
print w + e

