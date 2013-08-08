# Open a file
my_file = open("testtrunc.txt", "r+")

# truncate file.
my_file.truncate()

result = my_file.read()
print "Read Line:", result

my_file.close()


