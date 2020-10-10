from lib import asciify
from functions.printchar import printchar
from functions.printtext import printtext
from functions.writeraw import writeraw
from functions.flushcode import flushcode
from functions.storechar import storechar
import glob
import os.path
def portrait(imagepath):
  if not os.path.exists(imagepath):
    print("ERROR: file not found: "+imagepath)
  image=asciify.runner(imagepath)
  writeraw("[-]")
  glob.bitcounter=0
  
  writeraw(">")
  storechar(chr(27))
  writeraw(">")
  storechar('[')
  writeraw(">")
  storechar('1')
  writeraw(">")
  storechar('C')
  writeraw("<<<<")

  printtext(chr(27)+"[f")
  for x in range(0,len(image)):
    if (image[x]=='@'):
      writeraw(">.>.>.>.<<<<")
    else:
      printchar(image[x])
    if (x==138):
      printtext(chr(27)+"E")
  writeraw(">[-]>[-]>[-]>[-]<<<<")
  flushcode()