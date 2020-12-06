import time
import random


name = input("Hello, what is your name? ")

print("Hello " + name)

feeling = input("How are you today? ")

if 'good' in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")

favcolour = input("What is your favourite colour? ")

colours = ["Red", "Green", "Blue"]

print("My favourite colour is " + random.choice(colours))
