__author__ = 'MindBullets'
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