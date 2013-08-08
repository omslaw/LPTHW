# variable for cars
cars = 100
# variable for how much space in car
space_in_a_car = 4.0
# variable for number of drivers
drivers = 30
# variable for passengers in cars
passengers = 90
# variable for cars not driven, just sub the drivers from total of cars
cars_not_driven = cars - drivers
# variable for the total driven is the same as drivers
cars_driven = drivers
# variable for the carpool capacity which is the cars driven times the space in a car to get total volume
carpool_capacity = cars_driven * space_in_a_car
# variable for getting the average passengers versus cars driven
average_passengers_per_car = passengers / cars_driven


# prints out how many cars available
print "There are", cars, "cars available."
# prints out how many drivers are available
print "There are only", drivers, "drivers available."

print "There will be", cars_not_driven, "empty cars today."

print "We can transport", carpool_capacity, "people today."

print "We have", passengers, "to carpool today."

print "
