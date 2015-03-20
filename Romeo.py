__author__ = 'MindBullets'
try:
    fHand = open('romeo.txt', 'r')
except:
    print "No such file exists."
    exit()

wordList = list()
for line in fHand:
    line = line.rstrip()
    words = line.split()
    for i in range(len(words)):
        if words[i] not in wordList:
            wordList.append(words[i])
wordList.sort()
print wordList
fHand.close()

try:
    mBoxTxt = open('mbox.txt', 'r')
except:
    print "No such file exists."
    exit()

email = list()
eCounter = 0
for eLine in mBoxTxt:
    if not eLine.startswith("From"):
        continue
    curLine = eLine.split()
    email.append(curLine[1])
    eCounter += 1

print email
print "There were %d in the file starting with From." % (eCounter)

print "Modified this file in pycharm"
print "modified again"

print "modified and unstaged"
print "skipping staging area"

