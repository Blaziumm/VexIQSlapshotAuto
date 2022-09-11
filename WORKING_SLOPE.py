#X,Y
#No Decimals
goingcords = [3, 3]
def blockfinder(x,y):
  firstcords = [x, y]
  currentcords = 0
  ob = [1, 1]
  firstcordx = firstcords[0]
  firstcordy = firstcords[1]
  goingx = goingcords[currentcords]
  goingy = goingcords[currentcords + 1]
  xchange = goingx - firstcordx
  ychange = goingy - firstcordy
  if xchange == 0 and ychange == 0: 
    print('null')
    if x==ob[0] and y==ob[1]:
      blocked()
      return True
    return False
  elif xchange == 0 and ob[0] == firstcordx:
    if firstcordy <= ob[1] and ob[1] <= goingy:
      blocked()
      return True
  elif ychange == 0 and ob[1] == firstcordy:
    if firstcordx <= ob[0] and ob[0] <= goingx:
      blocked()
      return True
  repeat = 500
  testingx = float(firstcordx)
  testingy = float(firstcordy)
  finx = False
  finy = False

  for i in range (repeat):
      if testingx >= goingcords[currentcords]:
        finx = True
      if testingy >= goingcords[currentcords+1]:
        finy = True
      if finx and finy:
        if testingx == goingx and testingy == goingy:
            xmove = goingx - x 
            ymove = goingy - y
            print('X Move ', xmove)
            print('Y Move', ymove)
        return
      elif finy:
        if firstcordx <= ob[0] and ob[0] <= goingx and testingy == ob[1]:
          blocked()
          return True
        else:
          testingx += 0.5
          print('x',testingx)
          print('i',i)
      elif finx:
        if firstcordy <= ob[1] and ob[1] <= goingy and testingx == ob[0]:
          blocked()
          return True
        else:
          testingy += 0.5
          print('y',testingy)
          print('i',i)
      else:
        if testingx == ob[0] and testingy == ob[1]:
          blocked()
          return True
        else:
          testingx+=0.5
          testingy+=0.5
          print('x',testingx)
          print('i',i)
          print('y',testingy)
          print('i',i)
          
  return False

def blocked():
  print('blocked')
blockfinder(0,0)
