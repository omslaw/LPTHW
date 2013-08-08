# Function that takes two variables. 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints out the value of the first variable
    print "You have %d cheeses!" % cheese_count
    # prints out the value of the second variable
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # next two lines or just basic print statements
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# printing what the next test will be.
print "We can just give the function numbers directly:"
# giving two values to the function we created. it takes two values for each variable
cheese_and_crackers(20, 30)



# print what we are planning on doing next
print "OR, we can use variables from our script:"
# creating a variable we will use the first value for our function
amount_of_cheese = 10 
# creating the second variable that will be used as the second value for our function 
amount_of_crackers = 50

# here we use two newly created variables for the values of in our fuction
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# basic print statement of what we will be doing
print "We can even do math inside too:"
# calling the function and performing math to get the values that will be used
# with the example below it's like passing 30 and 11
cheese_and_crackers(10 + 20, 5 + 6)

# basic print statement about what is about to be done
print "And we can combine the two, variables and math:"
# use the variable we created earlier and math together to pass values to the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
