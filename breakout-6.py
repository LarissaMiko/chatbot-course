characters = ['Daisy Duck', 'Albert Einstein', 'John Lennon', 'Harry Potter',
              'Hermine Granger', 'Angela Merkel', 'Angelina Jolie', 'Barack Obama', 'Luigi', 'Super Mario']


print('Merk dir einen der folgenden Charaktere und ich werde ihn erraten: ')

for character in characters:
    print(character)

# Funktion, die Ja/nein antwort in boolean umwandelt


def getBool(ans):
    if 'ja' in ans.lower():
        return True
    else:
        return False


# Überlege, welche Kategorien es gibt und frage sie nacheinander ab
real = getBool(input('Gibt es deine Figur wirklich? '))

female = getBool(input('Interessant...Ist deine Figur weiblich?'))

human = False
politician = False
animal = False
mario = False
red = False

if real:
    if female:
        politician = getBool(input('Soso, und macht deine Figut Politik? '))
        if politician:
            print('Du denkst an Angela Merkel')
        else:
            print('Es ist Angelina Jolie')
    else:
        if politician:
            print('Du denkst an Barack Obama')
        else:
            print('Du denkst an John Lennon')
# if not real
else:
    if female:
        human = getBool(input('Ist deine Figur denn menschlich? '))
        if human:
            print('Deine Figur ist Hermine Granger')
        else:
            print('Deine Figur ist Daisy Duck')
    else:
        mario = getBool(input('Ist deine Figur ein Klempner? '))
        if mario:
            red = getBool(input('trägt deine Figur rot? '))
            if red:
                print('Es ist Mario')
            else:
                print('Es ist Luigi')
        else:
            print('Deine Figur ist Harry Potter')
