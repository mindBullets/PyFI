__author__ = 'MindBullets'

# 10.2 tuple assignment
txt = 'but soft what light in yonder window breaks'
txt = txt.split()
# build a list of tuples
t = list()
# add word length, word for each tuple then reverse it
for word in txt:
    t.append((len(word), word))
t.sort(reverse=True)
print(t)

# extract only the word then print
lst = list()
for wordLen, word in t:
    lst.append(word)
print(lst)

# ###################################################
# Exercises begin
# Exercise 10.1
def filePrompt():
    return input("Enter the file name: ")

def myOpen(openFile):
    return open(openFile, 'r')

myFile = filePrompt()
try:
    fHand = myOpen(myFile)
except:
    print("No such file or directory: %s" % (myFile))
    exit()

d = dict()
commitCount = 0

for line in fHand:
    # strips whitespace from left and write of string
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        # email = words[1]
        d[words[1]] = d.get(words[1], 0) + 1
print(d)

listOfTuples = list()
# data has been read now DSU
for key, val in d.items():
    listOfTuples.append((val, key))
listOfTuples.sort(reverse=True)
val, key = listOfTuples[0]
print('{0[1]} {0[0]}'.format(listOfTuples[0]))

# Exercises 10.2