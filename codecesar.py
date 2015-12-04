word = "elisha"
n = 5
wordlist = list(word)
new = []
for i in wordlist:
    j = list('abcdefghijklmnopqrstuvwxyz').index(i)
    j = (j + n)%25
    i = list('abcdefghijklmnopqrstuvwxyz')[j]
    new.append(i)
print new

word = "rfcaqtqt"
n = 5
wordlist = list(word)
new = []
for i in wordlist:
    j = list('abcdefghijklmnopqrstuvwxyz').index(i)
    j = (j - n)%25
    i = list('abcdefghijklmnopqrstuvwxyz')[j]
    new.append(i)
print new

