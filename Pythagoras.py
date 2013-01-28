import math

side = input ("Hvilken side skal du finde? ")

if side == "a":
    b = input ("Hvor lang er siden b? ")
    c = input ("Hvor lang er siden c? ")
    resultat = (ctal ** 2 - btal ** 2)
elif side == "b":
    a = input ("Hvor lang er siden a? ")
    c = input ("Hvor lang er siden c? ")
    resultat = (ctal ** 2 - atal ** 2)
elif side == "c":
    a = input ("Hvor lang er siden a? ")
    b = input ("Hvor lang er siden b? ")
    resultat = (atal ** 2 + btal ** 2)

atal = float(a)
btal = float(b)
ctal = float(c)

print ("Resultatet er: ", resultat)
