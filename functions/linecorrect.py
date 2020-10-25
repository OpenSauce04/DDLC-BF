import glob
def linecorrect(text):
  ctext = text
  for x in reversed(range(0, int(len(ctext)/glob.width))):
    i = 0
    if ctext[x*glob.width] != " ":
      while ctext[x*glob.width+i] != " ":
        i-=1
      text=text.split(" ")
      text.insert(x*glob.width+i, '\n')
      text=' '.join(text, )
  return text
