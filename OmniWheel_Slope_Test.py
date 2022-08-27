#Vex Omni Wheel Slope Test
#Made by Evan Wirzburger
#Team 21037A
#X,Y
firstcords = [0, 0]
goingcords = [2, 2, 3, 3]
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
        if testingx == ob[0]:
            if slope * testingx == ob[1]:
                print('Block')

        testingx += 0.5
        i += 1
        print('x', testingx)
        print('i', i)

    curentcords += 2
                


for l in range (funcrepeat):
    slopealg()
    l += 1
