language = input("Sprog/Language")
if language == "English" or language == "Engelsk":
    LANG = 1
else:
    LANG = 0

def firkantAreal(længde,bredde):
    areal = længde * bredde
    return areal
    
    
text1 = ("Hvad er længden?","What is the length")
text2 = ("Hvad er bredden?","What is the width")
text3 = ("Arealet er ","The area is ")


l = input(text1[LANG])
b = input(text2[LANG])
l = float(l)
b = float(b)
resultat = firkantAreal(l,b)
print (text3[LANG], resultat)



