import math

language = input ("Sprog/Language\n")
if language == "English" or language == "english":
    LANG = 1
elif language == "Dansk" or language == "dansk":
    LANG = 0

def andengradsligning():
    aValue = ("Hvad er a-værdien?\n", "What is the a-value?\n")
    aValue = input (aValue[LANG])

    bValue = ("Hvad er b-værdien?\n", "What is the b-value?\n")
    bValue = input (bValue[LANG])

    cValue = ("Hvad er c-værdien?\n", "What is the c-value?\n")
    cValue = input (cValue[LANG])

    aValue = float (aValue)
    bValue = float (bValue)
    cValue = float (cValue)

    #Diskriminatnenformel er: b^2-4ac

    discriminant = (bValue ** 2 - 4 * aValue * cValue)

    if (discriminant) < 0:
        ERROR = ("0 løsninger, diskriminatnen er negativ!", "0 solutions, the discriminant is negative!")
        print (ERROR[LANG])
    elif (discriminant) == 0:
        solution1 = ("1 løsning, diskriminaten er 0!", "1 solution, the discriminant is 0!")
        print (solution1[LANG])
    else:
        discriminantText = ("Diskriminanten er\n", "The discriminant is\n",)
        print (discriminantText[LANG], discriminant)

    result = ("Løsning 1 er:\n", "Solution 1 is:\n")
    print (result[LANG], (-bValue + (math.sqrt(discriminant)/(2*aValue))))
    result2 = ("Løsning 2 er:\n", "Solution 2 is:\n")
    print (result2[LANG], (-bValue - (math.sqrt(discriminant)/(2*aValue))))

    return    
andengradsligning()
