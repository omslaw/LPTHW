i = 0
numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i


# print "The numbers: "

# for num in numbers:
#    print num



def loop(x, times): 
    global i
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + times
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

loop(16, 3)

print "The numbers: "

for num in numbers:
    print num
