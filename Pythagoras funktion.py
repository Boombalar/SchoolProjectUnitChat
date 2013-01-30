import math

language = input ("Sprog/Language ")
if language == "English" or language == "english":
    LANG = 1
elif language == "Dansk" or language == "dansk":
    LANG = 0

side = ("Hvilken side vil du finde? ", "Which side do you want to find? ")
side = input (side[LANG])


if side == "a" or side == "A":
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


elif side == "b" or side == "B":
    def pythagorasB (pythagorasA, pythagorasC):
        if (pythagorasC) < (pythagorasA):
            text5 = ("Denne trekant er ikke 90 grader!", "This is not a 90 degree triangle!")
            input (text5[LANG])
        elif (pythagorasC) > (pythagorasA):
            pythagorasB = (math.sqrt(pythagorasC ** 2 - pythagorasA ** 2))
            return pythagorasB

    text6 = ("Hvor lang er side a? ", "How long is side a? ")
    text7 = ("Hvor lang er side c? ", "How long is side c? ")
    text8 = ("Side b er: ", "Side b is: ")

    pythagorasA = input(text6[LANG])
    pythagorasC = input(text7[LANG])
    pythagorasA = float(pythagorasA)
    pythagorasC = float(pythagorasC)
    resultat = pythagorasB (pythagorasA,pythagorasC)
    print (text8[LANG], resultat)


elif side == "c" or side == "C":
    def pythagorasC (pythagorasB, pythagorasA):
        pythagorasC = (math.sqrt(pythagorasA ** 2 + pythagorasB ** 2))
        return pythagorasC

    text9 = ("Hvor lang er side a? ", "How long is side a? ")
    text10 = ("Hvor lang er side b? ", "How long is side b? ")
    text11 = ("Side c er: ", "Side c is: ")

    pythagorasA = input(text9[LANG])
    pythagorasB = input(text10[LANG])
    pythagorasB = float(pythagorasB)
    pythagorasA = float(pythagorasA)
    resultat = pythagorasC (pythagorasB,pythagorasA)
    print (text11[LANG], resultat)


