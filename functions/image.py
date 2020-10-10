from lib import asciify
from functions.printtext import printtext
from functions.skipline import skipline
import os.path
def image(image):
  if not os.path.exists(image):
    print("ERROR: file not found: "+image)
  printtext(chr(27)+"[f")
  printtext(asciify.runner(image))
  skipline(6)