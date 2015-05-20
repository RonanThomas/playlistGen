# -*- coding: utf-8 -*-

#Import modules Python
import os

## Affiche un texte en rouge et en gras dans le terminal
#  @param output : String
def Redbold(output):
    os.system("tput bold")
    os.system("tput setaf 1")
    print(output)
    os.system("tput sgr 0")
   
## Affiche un texte en gras dans le terminal
#  @param output : String
def Bold(output):
    os.system("tput bold")
    print(output)
    os.system("tput sgr 0")
    
## Affiche un texte en rouge dans le terminal
#  @param output : String
def Red(output):
    os.system("tput setaf 1")
    print(output)
    os.system("tput sgr 0")
