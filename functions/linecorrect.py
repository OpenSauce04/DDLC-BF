def linecorrect(text):
  ctext=text
  for x in reversed(range(0,int(len(ctext)/150))):
    i = 0
    if ctext[x*150]!=" ":
      while ctext[x*150+i]!=" ":
        i-=1
      text=text.split(" ")
      text.insert(x*150+i,'\n')
      text=' '.join(text, )
      print(text)
  return text
