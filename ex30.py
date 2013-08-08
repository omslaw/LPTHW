# setup the variables
people = 30
cars = 40
buses = 15

# test if there are more cars than people
if cars > people:
    # if more cars than people then print this statement
    print "We should take the cars."
# if above is not true then this checks if cars are more than people
elif cars < people:
    # if that was true then print this
    print "We should not take the cars."
# if none of the above were true then print this statement. 
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

if people > buses and buses < cars:
    print "WTF Bitch!!!"
else:
    print "Nevermind"
