from functions.printchar import printchar
from functions.writeraw import writeraw
import glob
def printline(input):
  writeraw("[-]")
  glob.bitcounter=0
  for x in range(0,len(input)):
    printchar(input[x])
  printchar('\n')