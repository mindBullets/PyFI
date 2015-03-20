__author__ = 'MindBullets'
import string
# 9.4 advanced text parsing

d = dict()
fName = raw_input("Enter the file name: ")

try:
    handle = open(fName, 'r')
except:
    print "File cannot be opened: ", fName
    exit()

for line in handle:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        d[word] = d.get(word, 0) + 1

myKeys = d.keys()
myKeys.sort()

for key in myKeys:
    print "%s : %s" % (key, d[key])