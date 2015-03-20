def filePrompt():
    return raw_input("Enter the file name: ")

def myOpen(openFile):
    return open(openFile, 'r')

myFile = filePrompt()
try:

    fHand = myOpen(myFile)
except:
    print "No such file or directory: %s" % (myFile)
    exit()

notPrinted = 0
printed = 0
dSPAM = 0.0
confidence = 0.0

for line in fHand:
    # strips whitespace from left and write of string
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        notPrinted += 1
        continue
    dSPAM += float(line[line.find(':')+2::])
    printed += 1.0
    confidence = dSPAM/printed
print "DSPAM: %g / Count: %g = Average Confidence: %g" % (dSPAM, printed, confidence)