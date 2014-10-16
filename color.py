# -*- coding: utf-8 -*-

#Import modules Python
import os

def Redbold(output):
    os.system("tput bold")
    os.system("tput setaf 1")
    print(output)
    os.system("tput sgr 0")
    
def Bold(output):
    os.system("tput bold")
    print(output)
    os.system("tput sgr 0")
    
def Red(output):
    os.system("tput setaf 1")
    print(output)
    os.system("tput sgr 0")