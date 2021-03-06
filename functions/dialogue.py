from functions.printline import printline
from functions.printtext import printtext
from functions.printtext import printtext
from functions.writeraw import writeraw
from functions.clearline import clearline
from functions.skipline import skipline
from functions.linecorrect import linecorrect
from functions.debug import debug
def cleardialogue():
  for x in range(0,6):
    printtext(chr(27)+"[4"+str(3+x)+";0H")
    clearline()

def dialogue(speaking, text):
  debug(3, "Writing dialogue for "+speaking+": '"+text+"'")
  cleardialogue()
  printtext(chr(27)+"[43;0H")
  if not (speaking==""):
    printline('+'+('-'*(len(speaking)+2))+'+')
    printline("| "+speaking+" |")
  else:
    skipline(2)

  printline('+'+('-'*148)+'+')
  printtext(linecorrect(text))
  writeraw(">,[-]<")
