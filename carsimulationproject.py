print("WLCOME TO THE WORLD OF TATA")
sound=False
gear=0

while(True):
    print("--------MENU-------")
    print("START")
    print("STOP")
    print("CHANGE GEARS")
    print("BRAKE")
    print("QUIT")
    x = int(input("enter your choice"))
    if(x==1):
        if(sound==False):
            print("car started")
            sound=True
        else:
            print("car is already started")


    elif(x==2):
        if(sound==True):
            print("car stopped")
            sound=False
        else:
            print("car already stopped")

    elif(x==3):
        if(gear<=3):
            if (sound == True):
                print("gear shifted")
                gear=gear+1

            else:
                print("gear reduces")
        else:
            print("gear cant be shifted more")

    elif(x==4):
        if(sound==True):
            print("brakes applied")
        else:
            print("do not apply brakes in stop mode")

    elif(x==5):
        print("THANK YOU FOR USING OUR SERVICE")
        break

    else:
        print("please enter the correct choice")