import math
import sys

running = True

while running == True:
    side = input ("Hvilken side skal du finde? ")
    resultat = 0
    flag = True
    if side == "a":
        b = input ("Hvor lang er siden b? ")
        c = input ("Hvor lang er siden c? ")
        btal = float(b)
        ctal = float(c)
        if float(c) < float(b):
            print ("Dette er ikke en ret vinkel")
            flag = False
        elif float(c) > float(b):
            resultat = (math.sqrt(ctal ** 2 - btal ** 2))
    elif side == "b":
        a = input ("Hvor lang er siden a? ")
        c = input ("Hvor lang er siden c? ")
        atal = float(a)
        ctal = float(c)
        if float(c) < float(a):
                print ("Dette er ikke en ret vinkel")
                flag = False
        elif float(c) > float(a):
            resultat = (math.sqrt(ctal ** 2 - atal ** 2))
    elif side == "c":
        a = input ("Hvor lang er siden a? ")
        b = input ("Hvor lang er siden b? ")
        atal = float(a)
        btal = float(b)
        resultat = (math.sqrt(atal ** 2 + btal ** 2))
    if flag == True:
        print ("Resultatet er: ", resultat)

    fortsæt = input("Vil du fortsætte ")
    if fortsæt == "Ja" or fortsæt == "ja":
        running == True
    else:
        sys.exit(0)
