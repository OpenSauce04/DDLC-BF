from functions.printtext import printtext
import os.path
def preimage(path):
  if not os.path.exists(path):
    print("ERROR: file not found: "+path)
  f = open(path, "r")
  printtext(chr(27)+"[f")
  printtext(f.read())
  f.close