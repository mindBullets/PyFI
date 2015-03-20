__author__ = 'MindBullets'

fOutHand = open('output.txt', 'w')
print fOutHand
inString = ''
lineCount = 0
while inString != 'quit':
    inString = raw_input("Enter some text: ")
    fOutHand.write(inString + '\n')
    lineCount += 1

fOutHand.close()

fOutHand = open('output.txt', 'r')

for line in fOutHand:
    print line.rstrip()

fOutHand.close()
