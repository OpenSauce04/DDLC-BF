from functions.printchar import printchar
from functions.writeraw import writeraw
from functions.debug import debug
import glob
def printline(input):
  debug(2, "Writing line '"+input+"'")
  writeraw("[-]")
  glob.bitcounter=0
  for x in range(0,len(input)):
    printchar(input[x])
  printchar('\n')
