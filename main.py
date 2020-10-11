import init
import glob
from functions.printtext import printtext
from functions.preimage import preimage
from functions.writeraw import writeraw
from functions.skipline import skipline
from functions.flushcode import flushcode
from strings import *

try:
  open('DDLC-BF.bf', 'w').close() #wipe code
except:
  # previous file does not exist, continue
  True # Empty instruction to stop python from complaining
print("Compiling to './DDLC-BF.bf'...")

printtext(chr(27)+"[2J")
preimage("resources/prerenderedImages/configborder.txt")
writeraw(",") # Wait for key press
printtext(chr(27)+"[2J")
preimage("resources/prerenderedImages/titlescreen.txt")
skipline(3)
writeraw(",")

import chapters.chapter1

flushcode()
glob.f.close()

print("done.")