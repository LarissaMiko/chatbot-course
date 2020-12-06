characters = [
  {"name": "Minnie Mouse", "real": False, "female": True},
  {"name": "Meryl Streep", "real": True, "female": True},
  {"name": "Albert Einstein", "real": True, "female": False},
  {"name": "Harry Potter" , "real": False, "female": False}
  ]

# Funktion, die Ja/nein antwort in boolean umwandelt
def getBool(ans):
  if 'ja' in ans.lower():
    return True
  else:
    return False

print("Wähle einen der folgenden Charaktere und ich werde ihn erraten!")

for character in characters:
  print(character["name"])


realAntwort = input("Gibt es deine Figur wirklich ?")
real = getBool(realAntwort)
femaleAntwort = input("Soso...und ist deine Figur weiblich? ")
female = getBool(femaleAntwort)

for character in characters: 
  if character["real"] == real and character["female"] == female:
    print("Deine Figur ist " + character["name"])
