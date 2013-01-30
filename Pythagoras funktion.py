import math

language = input ("Sprog/Language ")
if language == "English " or language == "english ":
    LANG = 1
else:
    language == "Dansk " or language == "dansk "
    LANG = 0

def pythagorasA (pythagorasB, pythagorasC):
    if (pythagorasC) < (pythagorasB):
        text4 = ("Denne trekant er ikke 90 grader!", "This is not a 90 degree triangle!")
        input (text4[LANG])
    elif (pythagorasC) > (pythagorasB):
        pythagorasA = (math.sqrt(pythagorasC ** 2 - pythagorasB ** 2))
        return pythagorasA

text1 = ("Hvor lang er side b? ", "How long is side b? ")
text2 = ("Hvor lang er side c? ", "How long is side c? ")
text3 = ("Side a er: ", "Side a is: ")

pythagorasB = input(text1[LANG])
pythagorasC = input(text2[LANG])
pythagorasB = float(pythagorasB)
pythagorasC = float(pythagorasC)
resultat = pythagorasA (pythagorasB,pythagorasC)
print (text3[LANG], resultat)

