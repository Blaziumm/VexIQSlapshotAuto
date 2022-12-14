file1 = open("data.txt", "r")


data = file1.readlines()
cleandata = []
lines = len(file1.readlines())
string = ""
print(data)

for i in range(len(data)):
    print(i)
    string = data[i]
    string = string.replace("\n", "")
    print(string)
    for i in range(len(string)):
        if string[i] == "!":
            print("Truethat")
            if string[i+1].isnumeric():
                fowardvel = string[i+1]
                print("pass1")
                if string[i+2].isnumeric():
                    fowardvel = fowardvel + string[i+2]
                    print("pass2")
                    if string[i+3].isnumeric():
                        fowardvel = fowardvel + string[i+3]
                        print("pass3")
            fowardvel = int(fowardvel)
            print(fowardvel)

        if string[i] == "?":
            print("Truethat")
            if string[i+1].isnumeric():
                turnamount = string[i+1]
                print("pass1")
                if string[i+2].isnumeric():
                    turnamount = turnamount + string[i+2]
                    print("pass2")
                    if string[i+3].isnumeric():
                        turnamount = turnamount + string[i+3]
                        print("pass3")
            turnamount = int(turnamount)
            print(turnamount)
            





            lmotorvel = "lmotor.setvelocity(" + str(fowardvel) + "-" + str(turnamount) + ", PERCENT)" + "\n"
            rmotorvel = "rmotor.setvelocity(" + str(fowardvel) + "+" + str(turnamount) + ", PERCENT)" + "\n"
            file2 = open("code.txt")
            print(lmotorvel)
            print(rmotorvel)

