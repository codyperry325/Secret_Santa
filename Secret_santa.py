import numpy as np
from random import choice
import random as rd
from typing import Set
import sys

# text_file = input("What is the name of your file?: ")
text_file = "names.txt"

### 
# How to run this code:
# Create a file in Secret_Santa that has the names of the contestants
# Run Secret_santa.py using /python3 Secret_santa.py
# Open outcome.txt
# If by chance an error message comes up, run again and it will delete the file
###
def new_file():
     with open("Outcome.txt", "w") as out:
          out.write("Here is the list of secret santas: " + '\n')
          out.write("Santa ---------> Recipient" + "\n")
     out.close()

def import_names(file_name):
     file = file_name
     with open(file, "r+") as f:
          for line in f:
               line=line.split()
               santas.append(line[0])              

def create_list(file_name):
     global santas
     santas = []
     exclude = []
     import_names(text_file)
     length=len(santas)
     i = 0
     while i < length:
          remove = []
          remove.append(i)
          j = choice(list(set(range(0,length))-set(exclude)-set(remove)))
          print(i,j)
          if i != j:
               outcome = (santas[i] + " ---------> " + santas[j])
               exclude.append(j)
               with open("Outcome.txt", "a+") as out:
                    out.write(outcome + "\n")
                    i += 1

try:
     new_file()
     create_list(text_file)
except IndexError:
     print("1 fail")
     new_file()
     pass
     create_list(text_file)


