import init
import glob
from functions.printtext import printtext
from functions.preimage import preimage
from functions.writeraw import writeraw

preimage("resources/prerenderedImages/titlescreen.txt")
writeraw(",") # Wait for key press

f = open("DDLC-BF.bf", "w")
f.write(glob.output)
f.close()
