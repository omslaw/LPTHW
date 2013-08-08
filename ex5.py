name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %f inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
        age, height, weight, age + height + weight)

# Conversions to Centimeters and kilos

centi = 2.54 # one inch equals 2.54 centimeters
kilos = 0.45359237 # one pound equals that many kilos

print "He's %d in the US and %d cm just about everywhere else" % (height, height * centi)
print "He's %d lbs and in cocaine terms he's %d kilos" % (weight, weight * kilos)
