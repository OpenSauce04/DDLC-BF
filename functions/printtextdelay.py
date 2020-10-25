from functions.printchardelay import printchardelay
from functions.writeraw import writeraw
import glob
def printtextdelay(input):
  writeraw("[-]")
  glob.bitcounter=0
  for x in range(0,len(input)):
    printchardelay(input[x])