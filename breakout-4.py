import random

# 1 Liste von Fragen, wie es Nutzer geht
questions = [
    'Wie geht es dir heute?',
    'Na was geht?',
    "What's up?",
    'Geht es dir gut?',
]
print(random.choice(questions))
ans = input()
ans = ans.lower()

# 2 Liste positiver Wörter
positives = [
    'gut',
    'toll',
    'großartig',
    'fantastisch',
]

# 3 Give a positive answer to a question if any of the positive words is in the answer - iterate through lists and use Booleans
happy = False

for word in positives:
    if word in ans:
        happy = True

if happy == True:
    if 'nicht' in ans:
        print('Schade zu hören, kann ich dir weiterhelfen?')
    else:
        print('Toll, dass es dir gut geht!')
else:
    print('Oh nein! Mir geht es heute auch nicht so gut')
