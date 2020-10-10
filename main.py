import init
import glob
from functions.printline import printline
from functions.image import image
from functions.preimage import preimage
from functions.writeraw import writeraw
from functions.skipline import skipline
from functions.dialogue import dialogue
from functions.portrait import portrait
from strings import *

preimage("resources/prerenderedImages/configborder.txt")
writeraw(",") # Wait for key press
preimage("resources/prerenderedImages/titlescreen.txt")
skipline(3)
writeraw(",")
image("resources/images/bg/house.png")
dialogue("???",'"Heeeeeeeyyy!!"')
dialogue("",'"I see an annoying girl running toward me from the distance, waving her arms in the air like she`s totally oblivious to any attention she might draw to herself."')
dialogue("",'"That girl is Sayori, my neighbor and good friend since we were children."')
dialogue("",'"You know, the kind of friend you`d never see yourself making today, but it just kind of works out because you`ve known each other for so long?"')
dialogue("",'"We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."')
dialogue("",'"But if she`s going to chase after me like this, I almost feel better off running away."')
dialogue("",'"However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."')
portrait("resources/images/portrait/sayori/sayoriUwu.png")
dialogue(sayoriname,'"Haaahhh...haaahhh..."')
dialogue(sayoriname,'"I overslept again!"')
dialogue(sayoriname),'"But I caught you this time!"')
dialogue(mcname, '"Maybe, but only because I decided to stop and wait for you."')
f = open("DDLC-BF.bf", "w")
f.write(glob.output)
f.close()