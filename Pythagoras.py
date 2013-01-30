import math
import sys

running = True

while running == True:
    side = input ("which side do you want to find?\n")
    result = 0
    flag = True
    if side == "a" or side == "A":
        bString = input ("How long is side b?\n")
        cString = input ("How long is side c?\n")
        b = float(bString)
        c = float(cString)
        if (c) < (b):
            print ("This is not a 90 degree triangle")
            flag = False
        elif (c) > (b):
            result = (math.sqrt(c ** 2 - b ** 2))
            
    elif side == "b" or side == "B":
        aString = input ("How long is side a?\n")
        cString = input ("How long is side c?\n")
        a = float(aString)
        c = float(cString)
        if (c) < (a):
                print ("This is not a 90 degree triangle")
                flag = False
        elif (c) > (a):
            result = (math.sqrt(c ** 2 - a ** 2))
            
    elif side == "c" or side == "C":
        aString = input ("How long is side a?\n")
        bString = input ("How long is side b?\n")
        a = float(aString)
        b = float(bString)
        result = (math.sqrt(a ** 2 + b ** 2))
    if flag == True:

        print ("The result is:\n",result)
        
    print (" ")
    print ("Do you want to continue?")
    keeprunning = input ("Yes for continue   No for exit\n")
    if keeprunning == "Yes" or keeprunning == "yes":
        running == True
    else:
        sys.exit(0)
