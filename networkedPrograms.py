__author__ = 'MindBullets'
import socket
import time
import urllib.request

"""Super basic web browser
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('www.py4inf.com', 80))
mySock.send(bytes('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n', 'UTF-8'))

while True:
    data = mySock.recv(512)
    if len(data) < 1:
        break
    print(data)
mySock.close()
End super basic web browser"""

"""s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.py4inf.com', 80))
s.send(bytes('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n', 'UTF-8'))

count = 0
picture = bytes()

while True:
    data = s.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    picture += data
    count += len(data)
    print('LENGTH: {0} COUNT: {1}'.format(len(data), count))
s.close()

pos = picture.find(bytes('\r\n\r\n', 'utf8')) + 4 #find two carriage return new lines ie., CRLF 4 characters

print("Header length: {0} characters".format(pos))

picture = picture[pos:]
#print("Remaining data")
#print(picture)

try:
    fhand = open("myPicture.jpg", "wb") # wb is write binary
except:
    print("Failed to open file: {0}".format(fhand))

fhand.write(picture)
fhand.close()"""

# urllib
d = dict()
urlHand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in urlHand:
    words = line.decode().strip().split()
    #print(words)
    for word in words:
        d[word] = d.get(word, 0) + 1
print(d)