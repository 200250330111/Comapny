import os

def clearConsole():
        command = 'cls'
        os.system(command)

def ChangeCase(dir,mode):
        if mode == "Normal":
            if dir == 'd':
                newMode = 'FanControl'
                return newMode
            elif dir == 'a':
                newMode ='Normal'
                return newMode
            elif dir == 's':
                newMode ='Normal'
                return newMode
            elif dir == 'w':
                newMode = 'Normal'
                return newMode

        if mode == "FanControl":
            if dir == 'd':
                newMode = 'Temperature'
                return newMode
            elif dir == 'a':
                newMode = 'Normal'
                return newMode
            elif dir == 's':
                newMode = 'FanSpeed'
                return newMode
            elif dir == 'w':
                newMode ='FanControl'
                return newMode

        if mode == "FanSpeed":
            if dir == "d":
                newMode = 'FanRPM'
                return newMode
            elif dir == "w":
                newMode = 'FanControl'
                return newMode
            elif dir == 'a':
                newMode = 'Fanspeed'
                return newMode
        

        if mode == "FanRPM":
            if dir == "a":
                newMode = 'FanSpeed'
                return newMode
            elif dir == "w":
                newMode = 'FanControl'
                return newMode
            elif dir == 's':
                newMode ='FanRPM'
                return newMode
            elif dir == 'd':
                newMode = 'FanRPM'
                return newMode

        if mode == "Temperature":
            if dir == "a":
                newMode = 'FanControl'
                return newMode
            elif dir == 's':
                newMode = 'Temperature'
                return newMode
            elif dir == 'w':
                newMode = 'Temperature'
                return NewMode
            elif dir == 'd':
                newMode = 'Temperature'
                return newMode


def DisplayMode(mode):
    if mode == 'FanSpeed':
        print("Adjusting Fan speed\n")
    if mode == 'FanRPM':
        print("Display Fan Rpm\n")
    if mode == 'Temperature':
        print("Display Temperature\n")


newMode = 'Normal'
print(newMode)

while True:
    dir = input()
    Mode = ChangeCase(dir,newMode)
    newMode = Mode
    print("Changed to",Mode," mode")
    clearConsole()
    DisplayMode(Mode)
