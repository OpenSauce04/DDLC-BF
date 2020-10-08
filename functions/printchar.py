import glob;
def printchar(input):
  while (ord(input) != glob.bitcounter):
    if (ord(input)>glob.bitcounter):
      glob.output+="+"
      glob.bitcounter+=1
    else:
      glob.output+="-"
      glob.bitcounter-=1
  glob.output+="."