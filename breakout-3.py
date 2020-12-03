print("Wie heißt du?")
name = input()

print("Hallo, " + name)
print("Wie geht es dir, " + name + "?")
zustand = input()

if "gut" in zustand and "nicht" not in zustand: 
  print("Das ist schön zu hören!")

else:
  print("schade")