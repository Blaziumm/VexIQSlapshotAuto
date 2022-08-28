#X,Y
#No Decimals
firstcords = [0, 0]
goingcords = [3, 3, 3, 3, 4, 4]
funcrepeat = len(goingcords)//2
def slopealg():
    curentcords = 0
    ob = [1, 1]
    firstcordx = firstcords[0]
    firstcordy = firstcords[1]
    goingx = goingcords[curentcords]
    goingy = goingcords[curentcords + 1]
    xchange = goingx - firstcordx
    ychange = goingy - firstcordy
    slope = ychange//xchange

    repeat = int(xchange//0.5)
    testingx = float(firstcordx)

    for i in range (repeat):
        if testingx >= goingcords[curentcords]:
            break
        else:
            if testingx == ob[0]:
                if slope * testingx == ob[1]:
                    if testingx >= firstcords[0] and testingx <= goingcords[curentcords]:
                        print('Block')
                    else:
                        xmove = goingcords[curentcords] - firstcords[0]
                        xmove = goingcords[curentcords + 1] - firstcords[1]

                        firstcords[0] == goingcords[curentcords]
                        firstcords[1] == goingcords[curentcords + 1]

                        #PID.Drive.distance(xmove)
                        #PID.Drive.dostance(ymove)
                        
            testingx += 0.5
            i += 1
            print('x', testingx)
            print('i', i)

    curentcords += 2
                


for l in range (funcrepeat):
    slopealg()
    l += 1
