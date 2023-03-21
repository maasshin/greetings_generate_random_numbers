#!/usr/bin/env  python3

import random

def greetings():
  name = input("Halo!, Wie heißen Sie?")
  Woher = input("Wo Wohnen Sie?")
  Alter = input("Wie alt sind Sie?")
  Arbeite = input("Was arbeiten  Sie?") 
  Number = random.randint(2,111)
  print("Welcome," + name + " aus" + Woher + ",Sie sind" + str(Alter) + "Jahre alt und arbeite  als" + Arbeite )
  print("Diene glücklich Nummer ist: " + str(Number))
  print("Danke, Auf Wiedersehen!")

greetings()
  
