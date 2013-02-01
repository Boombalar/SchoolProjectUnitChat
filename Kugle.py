import math
LANG = 0
def ball():
    question = ("Hvad vil du vide: ", "What do you want to know: ")
    knowledge = input(question[LANG])
    knowledge = knowledge.lower()
    if knowledge == "area" or knowledge == "areal":
        area()
    elif knowledge == "radius":
        radius()
    elif knowledge == "rumfang" or knowledge == "volume":
        volume()
        
        


def area():
    question = ("Hvad kender du allerede: ","What do you all ready know: ")
    knowledge = input(question[LANG])
    knowledge = knowledge.lower()
    question2 = ("Hvad er " + knowledge+ "? ", "What is " + knowledge + "?")
    knowledge2 = input(question2[LANG])
    if knowledge == "radius":
        resultat = areaFromRadius(knowledge2)
    elif knowledge == "volume" or knowledge == "rumfang":
        resultat = areaFromVolume(knowledge2)

    print ("Resultatet er :", resultat)
        

def radius():
    question = ("Hvad kender du allerede: ","What do you all ready know: ")
    knowledge = input(question[LANG])
    knowledge = knowledge.lower()
    question2 = ("Hvad er " + knowledge + "? ", "What is " + knowledge + "?")
    knowledge2 = input(question2[LANG])
    if knowledge == "area" or knowledge == "areal":
        resultat = radiusFromArea(knowledge2)
    elif knowledge == "volume" or knowledge == "rumfang":
        resultat = radiusFromVolume(knowledge2)

    print ("Resultatet er :", resultat)
    
def volume():
    question = ("Hvad kender du allerede: ","What do you all ready know: ")
    knowledge = input(question[LANG])
    knowledge = knowledge.lower()
    question2 = ("Hvad er " + knowledge + "? ", "What is " + knowledge + "?")
    knowledge2 = input(question2[LANG])
    if knowledge == "radius":
        resultat = volumeFromRadius(knowledge2)
    elif knowledge == "area" or knowledge == "areal":
        resultat = volumeFromArea(knowledge2)

    print ("Resultatet er :", resultat) 
    

def radiusFromArea(area):
    area = float (area)
    radius = (Areal/(4*math.pi))**(1/2)
    return radius

def radiusFromVolume(rumfang):
    rumfang = float (rumfang)
    radius = (rumfang *(3/(4*math.pi)))**(1/3)
    return radius
    

def areaFromRadius(radius):
    radius = float (radius)
    area = 4 * math.pi * radius**2
    return area

def areaFromVolume(rumfang):
    rumfang = float (rumfang)
    radius = radiusFromVolume(rumfang)
    area = areaFromRadius(radius)
    return area
    

def volumeFromRadius(radius):
    radius = float (radius)
    volume = (4/3) * math.pi * radius**3
    return volume

def volumeFromArea(area):
    area = float(area)
    radius = radiusFromArea(area)
    volume = volumeFromRadius(radius)
    return area

ball()
