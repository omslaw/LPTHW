print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Give it honey."
    print "4. Give it honey laced with poison."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3" or bear == "4":
        print "The bear spits out the cheese cake and goes for the honey."
        if bear == "3":
            print "The bear loves the honey and you have made a new friend."
            print "His name is Gentle Ben."
        else:
            print "The bear looks up at you and sheds a tear as it dies." 
            print "All it wanted was some honey."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == 3 or door == 4:
    print "The bear spits out the cheese cake and goes for the honey."

    if door == 4:
        print "The bear looks up at you and sheds a tear as it dies." 
        print "All it wanted was some honey."
    else:
        print "The bear loves the honey and you have made a new friend."
        print "His name is Gentle Ben."

else: 
    print "You stumble around and fall on a knife and die. Good job!"
