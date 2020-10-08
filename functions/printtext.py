from functions.printchar import printchar
def printtext(input):
  for x in range(0,len(input)):
    printchar(input[x])
  printchar('\n')