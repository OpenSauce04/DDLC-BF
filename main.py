import init
import glob
from functions.printtext import printtext
from functions.image import image
from functions.preimage import preimage
from functions.writeraw import writeraw
from functions.skipline import skipline
from functions.dialogue import dialogue
from functions.portrait import portrait
from functions.flushcode import flushcode
from strings import *

try:
  open('DDLC-BF.bf', 'w').close() #wipe code
except:
  # previous file does not exist, continue
  True # Empty instruction to stop python from complaining


printtext(chr(27)+"[2J")
preimage("resources/prerenderedImages/configborder.txt")
writeraw(",") # Wait for key press
printtext(chr(27)+"[2J")
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
portrait("resources/images/portrait/sayori/sayori1.png")
dialogue(sayoriname,'"Haaahhh...haaahhh..."')
dialogue(sayoriname,'"I overslept again!"')
dialogue(sayoriname,'"But I caught you this time!"')
dialogue(mcname, '"Maybe, but only because I decided to stop and wait for you."')
image("resources/images/bg/house.png")
portrait("resources/images/portrait/sayori/sayori2.png")
dialogue(sayoriname,'"Eeehhhhh, you say that like you were thinking about ignoring me!"')
dialogue(sayoriname, '"That`s mean, '+mcname+'!"')
dialogue(mcname, '"Well, if people stare at you for acting weird then I don`t want them to think we`re a couple or something."')
image("resources/images/bg/house.png")
portrait("resources/images/portrait/sayori/sayori3.png")
dialogue(sayoriname, '"Fine, fine."')
dialogue(sayoriname, '"But you did wait for me, after all."')
dialogue(sayoriname, '"I guess you don`t have it in you to be mean even if you want to~"')
dialogue(mcname, '"Whatever you say, Sayori..."')
image("resources/images/bg/house.png")
portrait("resources/images/portrait/sayori/sayori4.png")
dialogue(sayoriname, '"Ehehe~"')
image("resources/images/bg/house.png")
dialogue("", '"We cross the street together and make our way to school."')
dialogue("", '"As we draw near, the streets become increasingly speckled with other students making their daily commute."')
portrait("resources/images/portrait/sayori/sayori5.png")
dialogue(sayoriname, '"By the way, '+mcname+'..."')
dialogue(sayoriname, '"Have you decided on a club to join yet?"')
dialogue(mcname, '"A club?"')
dialogue(mcname, '"I told you already, I`m really not interested in joining any clubs.')
dialogue(mcname, '"I haven`t been looking, either."')
image("resources/images/bg/house.png")
portrait("resources/images/portrait/sayori/sayori6.png")
dialogue(sayoriname, '"Eh? That`s not true!"')
dialogue(sayoriname, '"You told me you would join a club this year!"')
dialogue(mcname, '"Did I...?"')
dialogue("", '"I`m sure it`s possible that I did, in one of our many conversations where I dismissively go along with whatever she`s going on about."')
dialogue("", '"Sayori likes to worry a little too much about me, when I`m perfectly content just getting by on the average while spending my free time on games and anime."')

flushcode()
glob.f.close()