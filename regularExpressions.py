import re
"""Example
try:
    fHand = open('mbox-short.txt', 'r')
except:
    print('No such file or directory exists: {0}'.format(fHand))
    exit()

email = list()
for line in fHand:
    email = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(email) > 0:
        print(email)
fHand.close()"""

"""Chapter 11 Exercises"""
# Ask the user to enter a regular expression and count the lines that matched
cmd = input("Enter a regular expression: ")

try:
    regHand = open('mbox.txt', 'r')
except:
    print('Error opening file: {0}'.format(regHand))

count = 0
for line in regHand:
    lst = re.findall(cmd, line)
    count += len(lst)
print('mbox.txt had {0} lines that matched {1}'.format(count, cmd))


# Write a program to look for the lines of the form:
# New Revision: 39772
# Extract the numbers and compute the average
myFile = input('Enter a file to open: ')
try:
    fHand = open(myFile,'r')
except:
    print('No such file exists: {0}'.format(fHand))
    exit()
total = 0.0
count = 0.0
for line in fHand:
    numList = re.findall('New Revision: ([0-9]+)', line) # re.findall returns a list so you need to for loop through
    if len(numList) > 0:
        for num in numList:
            total += float(num)
            count += 1
avg = total / count
print(avg)
"""End Exercises"""

