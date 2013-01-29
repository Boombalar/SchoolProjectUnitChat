import math
import sys

running = True

while running == True:
    side = input ("which side do you want to find? ")
    result = 0
    flag = True
    if side == "a" or side == "A":
        bString = input ("How long is side b? ")
        cString = input ("How long is side c? ")
        b = float(bString)
        c = float(cString)
        if (c) < (b):
            print ("This is not a 90 degree triangle")
            flag = False
        elif (c) > (b):
            result = (math.sqrt(c ** 2 - b ** 2))
    elif side == "b" or side == "B":
        aString = input ("How long is side a? ")
        cString = input ("How long is side c? ")
        a = float(aString)
        c = float(cString)
        if (c) < (a):
                print ("This is not a 90 degree triangle")
                flag = False
        elif (c) > (a):
            result = (math.sqrt(c ** 2 - a ** 2))
    elif side == "c" or side == "C":
        aString = input ("How long is side a? ")
        bString = input ("How long is side b? ")
        a = float(aString)
        b = float(bString)
        result = (math.sqrt(a ** 2 + b ** 2))
    if flag == True:
        print ("The result is: ", result)

    print (" ")    
    print ("Yes for continue     No for exit")
    keeprunning = input("Do you want to continue? ")
    if keeprunning == "Yes" or keeprunning == "yes":
        running == True
    else:
        sys.exit(0)
