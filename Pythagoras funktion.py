import math

language = input ("Sprog/Language\n")
if language == "English" or language == "english":
    LANG = 1
elif language == "Dansk" or language == "dansk":
    LANG = 0

side = ("Hvilken side vil du finde?\n", "Which side do you want to find?\n")
side = input (side[LANG])


if side == "a" or side == "A":
    def pythagorasA (pythagorasB, pythagorasC):
        if (pythagorasC) < (pythagorasB):
            ERROR = ("Denne trekant er ikke 90 grader!", "This is not a 90 degree triangle!")
            input (ERROR[LANG])
        elif (pythagorasC) > (pythagorasB):
            pythagorasA = (math.sqrt(pythagorasC ** 2 - pythagorasB ** 2))
            return pythagorasA

    sideB = ("Hvor lang er side b?\n", "How long is side b?\n")
    sideC = ("Hvor lang er side c?\n", "How long is side c?\n")
    sideA = ("Side a er:\n", "Side a is\n")

    pythagorasB = input(sideB[LANG])
    pythagorasC = input(sideC[LANG])
    pythagorasB = float(pythagorasB)
    pythagorasC = float(pythagorasC)
    resultat = pythagorasA (pythagorasB,pythagorasC)
    print (sideA[LANG], resultat)


elif side == "b" or side == "B":
    def pythagorasB (pythagorasA, pythagorasC):
        if (pythagorasC) < (pythagorasA):
            ERROR = ("Denne trekant er ikke 90 grader!", "This is not a 90 degree triangle!")
            input (ERROR[LANG])
        elif (pythagorasC) > (pythagorasA):
            pythagorasB = (math.sqrt(pythagorasC ** 2 - pythagorasA ** 2))
            return pythagorasB

    sideA = ("Hvor lang er side a?\n", "How long is side a?\n")
    sideC = ("Hvor lang er side c?\n", "How long is side c?\n")
    sideB = ("Side b er:\n", "Side b is:\n")

    pythagorasA = input(sideA[LANG])
    pythagorasC = input(sideC[LANG])
    pythagorasA = float(pythagorasA)
    pythagorasC = float(pythagorasC)
    resultat = pythagorasB (pythagorasA,pythagorasC)
    print (sideB[LANG], resultat)


elif side == "c" or side == "C":
    def pythagorasC (pythagorasB, pythagorasA):
        pythagorasC = (math.sqrt(pythagorasA ** 2 + pythagorasB ** 2))
        return pythagorasC

    sideA = ("Hvor lang er side a?\n", "How long is side a?\n")
    sideB = ("Hvor lang er side b?\n", "How long is side b?\n")
    sideC = ("Side c er:\n", "Side c is:\n")

    pythagorasA = input(sideA[LANG])
    pythagorasB = input(sideB[LANG])
    pythagorasB = float(pythagorasB)
    pythagorasA = float(pythagorasA)
    resultat = pythagorasC (pythagorasB,pythagorasA)
    print (sideC[LANG], resultat)


