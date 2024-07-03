open('fruits.txt','x')
filename = 'fruits.txt'


import os
os.path.exists(filename)
from os import path
path.exists(filename)
from os.path import exists
exists(filename)

def createFile(filename):
    if not exists(filename):
        try:
            open(filename,'x')
        except Exception as e:
            print("Something went wrong when we create the file",e)

filename = 'fruits.txt'
createFile(filename)







