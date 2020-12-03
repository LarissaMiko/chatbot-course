# Baue deinen eigenen Chatbot!

Aleksa, Siri &Co. : Chatbots sind überall. Doch wie schaffen sie es, uns die passenden Antworten auf unsere Fragen zu geben? Und wie lassen sie sich vielleicht auch austricksen?
Wir gehen diesen Fragen auf den Grund, indem wir unseren eigenen Chatbot von Grund auf selber bauen. Dafür benutzen wir die Programmiersprache Python.
Wie soll euer Bot reagieren, bekommt er vielleicht sogar einen ganz eigenen Charakter? Eurer Kreativität sind keine Grenzen gesetzt!

## Aufgabe 1: Lerne einen ersten Chatbot kennen!

---

**Was ist ein Chatbot?**: Ein Chatbot ist ein Computerprogramm, das ein Gespräch mit menschlichen Nutzern simulieren soll.

Können Computer „denken“?

Turing Test: Test, wie gut ein chatbot ist -> Kann eine Testperson unterscheiden, ob eine andere Person oder eine Maschine antwortet?

Welche Chatbots kennt ihr? (Alexa, Google Assistant, Siri)

Welche Nutzen haben Chatbots? (Suchmaschinen, Personal Assistent, (Emotional Support), Online-Handel, Assistenten zB im Projektmanagement)

### 1. Breakout-Session:

---

Schauen wir uns einen ersten Chatbot selber an: Geht auf https://de.akinator.com/ und
schaut, ob der Bot euere Figur/ Tier erraten kann.

Geh auf https://www.pandorabots.com/mitsuku/ und chattet mit „Mitsuku“ -> Was fällt
Euch auf? Was wäre anders, wenn ihr mit einem normalen Menschen chatten würdet?

Chatbots arbeiten mittels sogenanntem Natural Language Processing (NLP):

- Spracherkennung (speech recognition)
- Verstehen von Sprache (natural language understanding):
  Entscheidungen treffen auf Basis des Nutzerinputs
- Generieren ‚natürlicher‘ Sprache (natural language generation):
  Dem Nutzer soll mit verständlichem Text geantwortet werden

### 1. Code-Beispiel: 01-firstbot.py: Variablen, if/else

### 2. Breakout-Session: Smalltalk

---

Schreibe ein Programm, das den Nutzer zunächst nach seinem Namen fragt.
Verwende den eingegebenen Namen, um den Nutzer anzusprechen und stelle zwei Fragen, die richtig oder falsch beantwortet werden können. Antworte dem Nutzer entsprechend. Das Gespräch könnte zB so anfangen:

    Bot: „Wie heißt du?“
    Nutzer: „Alice“
    Bot: „Hallo Alice, was ist die Hauptstadt von Lettland?
    Nutzer: „Talinn“
    Bot: „Das stimmt nicht. Die Hauptstadt von Lettland ist Riga.“

## String-Manipulationen, Logische Verknüpfungen

---

Um besser auf die Antworten der Nutzer eingehen zu können, müssen wir die Antworten genauer analysieren können.
Hätte der Nutzer im letzten Beispiel geantwortet „Die Hauptstadt von Lettland ist Riga“, wäre die Antwort zwar richtig gewesen, der Bot hätte es aber nicht erkannt.

- Prüfe, ob ein bestimmter string in der Antwort ist
- Logische Verknüpfungen (and, or)
- Stringmanipulationen: lower(), upper()

### 3.Breakout-Session: „Wie geht es dir heute?“

---

Unser Bot soll ein bisschen empathischer werden. Frage den Nutzer wie es ihm geht und antworte entsprechend. Berücksichtige die verschiedenen Antworten, die ein Nutzer geben könnte („Mir geht es super!“ , „Mir geht es furchtbar!“ , „Heute geht es mir nicht so gut“)

Listen, For-Schleifen

Unser Bot erscheint natürlicher, wenn er nicht immer nur die gleichen Antworten gibt. Wir wollen mehrere Antwortmöglichkeiten zur Verfügung stellen und zufällig auswählen was geantwortet wird.

- import random, random.choice()
- Listen, zufälliges element wählen
- Booleans
- For-Schleifen

### 4.Breakout-Session: Bring Variation ins Gespräch!

---

Wir erweitern den Bot aus der letzten Breakout Session:

- Erstelle eine Liste von Fragen, um herauszufinden, wie es dem Nutzer geht
- Eine dieser Fragen soll zufällig gestellt werden

Optional (je nach Fortschritt):

- Erstelle Listen mit positiven und negativen Zuständen
- Erstelle eine boolean-Variable „happy“ , die dafür steht, ob es dem Nutzer gut geht
- Erstelle jeweils eine Liste mit positiven
- Gehe mit einer for-Schleife alle positiven Wörter durch und schau, ob sie in der Antwort des Nutzers vorkommen und setze in diesem Fall happy = True
- Prüfe, ob der Nutzer happy ist (happy = True) und antworte entsprechend („Freut mich zu hören“/ „Schade, das zu hören“)

Expert challenge: Prüfe zusätzlich, ob das Wort „nicht“ in der Antwort ist (zB. „Mir geht es gar nicht toll“)  Dann soll der Bot natürlich auf nicht-happy reagieren

## While-Schleifen

---

- While Schleifen
- numbers (integer, float)
- random.randint()

### Breakout-Session 5: Eine Zahl erraten

---

Speicher eine zufällige Zahl (zwischen 1 und 10) als Variable, die sich der Bot „denkt“ und lass den Nutzer diese erraten.
Frage immer weiter, solange der Nutzer die Zahl noch nicht erraten hat

Expert Challenge: Variiere die Antworten des Bot je nachdem, wie schnell der Nutzer die Zahl errät (z.B. Wenn die Zahl gleich beim ersten mal richtig ist: „Das ging aber schnell“)

## Funktionen

---
