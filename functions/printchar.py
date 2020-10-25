from os import write
from functions.writeraw import writeraw
import glob
def printchar(input):
  while (ord(input) != glob.bitcounter):
    if (ord(input)>glob.bitcounter):
      writeraw("+")
      glob.bitcounter+=1
    else:
      writeraw("-")
      glob.bitcounter-=1
  writeraw(".")
