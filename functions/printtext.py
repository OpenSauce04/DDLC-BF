from functions.printchar import printchar
from functions.writeraw import writeraw
import glob
def printtext(input):
  writeraw("[-]")
  glob.bitcounter=0
  for x in range(0,len(input)):
    printchar(input[x])