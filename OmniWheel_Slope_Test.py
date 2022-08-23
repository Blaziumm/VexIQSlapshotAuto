#Vex Omni Wheel Slope Test
#Made by Evan Wirzburger
#Team 21037A

#Cords Set Up
#This is your current Coords
firstx = 0
firsty = 0
#This is the Coords you are going to (Turning into a list)
Secondx = 1
Secondy = 1
#Obsticals (Turning into a list)
obx = 1
oby = 1

#Slope Calculations
changeinx = firstx - Secondx
changeiny = firsty - Secondy
slope = changeiny//changeinx

#Loop Prep
testingx = changeinx
repeatamount = Secondx

for i in range (50000):
    ycord = slope * testingx
    if ycord == oby and testingx == obx:
        if testingx >= firstx and testingx <= Secondx:
            print('True Block')
            break
        else:
            print('On slope but not Between Values')
        testingx = testingx + 0.5
        i = i + 1
        break
    testingx = testingx + 1
    i = i + 1
        

