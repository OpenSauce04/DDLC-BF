import init
import glob
from functions.printtext import printtext
from functions.image import image
from functions.preimage import preimage
from functions.writeraw import writeraw
from functions.clear import clear

preimage("resources/prerenderedImages/titlescreen.txt")
clear(6)
writeraw(",") # Wait for key press
image("resources/images/house.png")
clear(4)

f = open("DDLC-BF.bf", "w")
f.write(glob.output)
f.close()
