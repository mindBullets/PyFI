__author__ = 'MindBullets'
txt = 'but soft what light in yonder window breaks'
# build a list of tuples

txt = txt.split()
t = list()

for word in txt:
    t.append((len(word), word))

t.sort(reverse=True)
print(t)

lst = list()
for wordLen, word in t:
    lst.append(word)

print(lst)