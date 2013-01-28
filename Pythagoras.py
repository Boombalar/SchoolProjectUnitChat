import math

side = input ("Hvilken side skal du finde? ")

if side == "a":
    b = input ("Hvor lang er siden b? ")
    c = input ("Hvor lang er siden c? ")
    btal = float(b)
    ctal = float(c)
    resultat = (ctal ** 2 - btal ** 2)
elif side == "b":
    a = input ("Hvor lang er siden a? ")
    c = input ("Hvor lang er siden c? ")
    atal = float(a)
    ctal = float(c)
    resultat = (ctal ** 2 - atal ** 2)
elif side == "c":
    a = input ("Hvor lang er siden a? ")
    b = input ("Hvor lang er siden b? ")
    atal = float(a)
    btal = float(b)
    resultat = (atal ** 2 + btal ** 2)

print ("Resultatet er: ", resultat)
