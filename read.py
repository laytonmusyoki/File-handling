import os

""" file=open('layton.txt','r')
# print(file.read())
print(file.readline())
print(file.readlines())
file.close()

 """
with open('layton.txt','r') as f:
    for line in f:
        print(line)