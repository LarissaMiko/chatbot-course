import random

x = random.randint(1, 10)

print("Ich denke mir eine Zahl zwischen 1 und 10")
erraten = False
versuche = 0


def giveAnswer(versuche):
    if versuche < 3:
        return "Wow, das ging schnell!!"
    if versuche < 5:
        return "Richtig geraten!"
    if versuche < 7:
        return "Naja, blieb ja nicht mehr viel übrig"
    else:
        return "Stimmt, aber du bist nicht besonders gut im Raten"


while erraten == False:
    if versuche == 0:
        print('Welche Zahl ist es?')
    else:
        print("Nein, versuch es noch einmal!")

    antwort = input()
    if int(antwort) == x:
        print(giveAnswer(versuche))
        erraten = True
    else:
        versuche += 1
