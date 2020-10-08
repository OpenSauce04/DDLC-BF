from functions.printtext import printtext
def preimage(path):
  f = open(path, "r")
  printtext(f.read())
  f.close