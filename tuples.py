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

def myClose(closeHand):
    closeHand.close()

myFile = filePrompt()
try:
    fHand = myOpen(myFile)
except:
    print("No such file or directory: %s" % (myFile))
    exit()

d = dict()

for line in fHand:
    # strips whitespace from left and write of string
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        # email = words[1]
        d[words[1]] = d.get(words[1], 0) + 1

listOfTuples = list()
# data has been read now DSU
for key, val in d.items():
    listOfTuples.append((val, key))
listOfTuples.sort(reverse=True)
val, key = listOfTuples[0]
print('{0[1]} {0[0]}'.format(listOfTuples[0]))
myClose(fHand)

# Exercises 10.2
myFile = filePrompt()
try:
    fHand = myOpen(myFile)
except:
    print("No such file or directory: {0}" % (myFile))
    exit()

d = dict()

for line in fHand:
    # strips whitespace from left and write of string
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hourMinSec = time.split(':')
        d[hourMinSec[0]] = d.get(hourMinSec[0], 0) + 1

listOfHours = list()
# data has been read now DSU
for hour, count in d.items():
    listOfHours.append((hour, count))
listOfHours.sort()

print('Hour | Count')
print('============')
for hour, count in listOfHours:
    print('{0}     {1}'.format(hour, count))
myClose(fHand)