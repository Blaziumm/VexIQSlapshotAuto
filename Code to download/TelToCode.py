file1 = open("data.txt", "r")
rvel = ""
lvel = ""
data = file1.readlines()
cleandata = []
lines = len(data)
string = ""
time = ""
nexttime = ""
file1.close()
def velcheck(i):
    global rvel
    global lvel
    if string[i+1].isnumeric():
        rvel = string[i+1]
        if string[i+2] == ",":
            if string[i+3].isnumeric():
                lvel = string[i+3]
                if string[i+4].isnumeric():
                    lvel = lvel + string[i+4]   
                    if string[i+5].isnumeric():
                        lvel = lvel + string[i+5]
                
                
#break
        if string[i+2].isnumeric():
            rvel = rvel + string[i+2]
            if string[i+3] == ",":
                if string[i+4].isnumeric():
                    lvel = string[i+4]
                    if string[i+5].isnumeric():
                        lvel = lvel + string[i+5]   
                        if string[i+6].isnumeric():
                            lvel = lvel + string[i+6]
                                        
                                        
            if string[i+3].isnumeric():
                rvel = rvel + string[i+3]
                if string[i+4] == ",":
                    if string[i+5].isnumeric():
                        lvel = string[i+5]
                        if string[i+6].isnumeric():
                            lvel = lvel + string[i+6]   
                            if string[i+7].isnumeric():
                                lvel = lvel + string[i+7]
                        
for i in range(len(data)-1):
    string = data[i]
    nextline = data[i+1]
    string = string.replace("\n", "")
    nextline = nextline.replace("\n", "")
    for i in range(len(string)):
        if string[i] == "Y":
        
             if string[i+1].isnumeric():
                time = string[i+1]
                
                if string[i+2].isnumeric():
                    time = time + string[i+2]
                    try:
                        if string[i+3] == ",":
                            velcheck(i+3);
                           
                    except IndexError:
                        print("out of range")
                    if string[i+3].isnumeric():
                        time = time + string[i+3]
                        try:
                            if string[i+4] == ",":
                                velcheck(i+4);
                                
                        except IndexError:
                            print("out of range")
                        if string[i+4].isnumeric():
                            time = time + string[i+4]
                            try:
                                if string[i+5] == ",":
                                    velcheck(i+5);
                                   
                            except IndexError:
                                print("out of range")
                            if string[i+5].isnumeric():
                                time = time + string[i+5]
                                try:
                                    if string[i+6] == ",":
                                        velcheck(i+6);
                                    
                                except IndexError:
                                    print("out of range")
                        
                else:
                    if string[i] == ",":
                        velcheck(i+2);
                        
        try:                
            if nextline[i] == "Y":
              
            
                if nextline[i+1].isnumeric():
                    nexttime = nextline[i+1]
                    print(nexttime)
                    if nextline[i+2].isnumeric():
                        nexttime = nexttime + nextline[i+2]
        except IndexError:
            print("error")

    if rvel == lvel:
        print("nexttime")
        print(nexttime)
        print("time")
        print(time)
        time = int(nexttime) - int(time)
        print("time")
        print(time)
        output = "fowardvel(" + str(rvel)+ "," + str(time) + ")\n"
        print(output)
    else:
        output = "rmotor.set_velocity(" + rvel + ", PERCENT) \n"
        output2 = "lmotor.set_velocity(" + lvel + ", PERCENT) \n"
        time = int(nexttime) - int(time)
        output3 = "wait(" + str(time) + ", MSEC) \n"
        print(output)
        print(output2)
        print(output3)

    file1 = open("code.txt", "a")
    file1.write(output)
    try:
        file1.write(output2)
        file1.write(output3)
        file1.close()
    
    except NameError:
        pass
            



