import init
import glob
from functions.printline import printline
from functions.image import image
from functions.preimage import preimage
from functions.writeraw import writeraw
from functions.skipline import skipline
from functions.dialogue import dialogue

preimage("resources/prerenderedImages/configborder.txt")
writeraw(",") # Wait for key press
preimage("resources/prerenderedImages/titlescreen.txt")
skipline(3)
writeraw(",")
image("resources/images/house.png")
dialogue("???",'"Heeeeeeeyyy!!"')
dialogue("",'"I see an annoying girl running toward me from the distance, waving her arms in the air like she`s totally oblivious to any attention she might draw to herself."')
dialogue("",'"That girl is Sayori, my neighbor and good friend since we were children."')

f = open("DDLC-BF.bf", "w")
f.write(glob.output)
f.close()