# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

s = input('enter string: ')
s1 = ''
for x in s:
    if x.islower():
        s1+=x.upper()
    else:
        s1+=x.lower()
print(s1)