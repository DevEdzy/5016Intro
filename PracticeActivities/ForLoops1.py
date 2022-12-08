# ForLoops1.py
#
# author: Michael Edwards
# date: 14/11/2022

l = []

for i in range(1500, 2700):
    if (i % 7 == 0) and (i % 5 == 0):
        l.append(i)

print(l)
