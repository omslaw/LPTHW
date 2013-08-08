"""
def outFile(output):

    file = open("xtest.txt", 'a')
    line = (output)
    file.write(line)
    file.write("\n")
    file.close()

outFile("hiii")

"""

def test(penguin=None, x="example", b=None):
    if penguin is None and b is None:
        print "nada on both"
    else:
        print penguin
    #return penguin
