from functions.printline import printline
from functions.printtext import printtext
from functions.writeraw import writeraw
from functions.clearline import clearline
def cleardialogue():
  for x in range(0,6):
    printtext(chr(27)+"[4"+str(3+x)+";0H")
    clearline()

def dialogue(speaking, text):
  cleardialogue()
  printtext(chr(27)+"[43;0H")
  if not (speaking==""):
    printline('+'+('-'*(len(speaking)+2))+'+')
    printline("| "+speaking+" |")
  printline('+'+('-'*148)+'+')
  printtext(text)
  writeraw(">,[-]<")