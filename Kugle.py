import math

road = input ("Hvad vil du finde?   ")
if road == ("Overfladeareal"):
    Radius = input (" Hvad er din radius?  ")
    Radius = float (Radius)
    A = 4 * math.pi * Radius**2
    print (A)
elif road == ("Rumfang"):
    Rumfang = input ("Hvad er din radius?   ")
    Rumfang = float (Radius)
    V = (3/4) * math.pi * Radius**3
    print (V)
elif road == ("Radius ved hjælp af overfladeareal"):
    Areal= input ("Hvad er dit Areal?      ")
    Areal= float (Areal)
    ra = (Areal/(4*math.pi))**(1/2)
    print (ra)
elif road == ("Radius ved hjælp af rumfang"):
    Rumfang= input ("Hvad er dit rumfang?  ")
    Rumfang= float (Rumfang)
    rv = (Rumfang *(3/(4*math.pi)))**(1/3)
    print (rv)
