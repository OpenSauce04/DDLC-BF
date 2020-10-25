from lib import asciify
from functions.printtext import printtext
from functions.skipline import skipline
from functions.flushcode import flushcode
from functions.debug import debug
import os.path
def image(image):
  debug(3, "Writing image at '"+image+"'")
  if not os.path.exists(image):
    print("ERROR: file not found: "+image)
  printtext(chr(27)+"[f")
  printtext(asciify.runner(image))
  skipline(6)
  flushcode()
