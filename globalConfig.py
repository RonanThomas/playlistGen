# -*- coding: utf-8 -*-

"""Ce module permet de récupérer le fichier de config, si il existe """

#Import modules Python
import os
import sys

#Import modules Projet
from color import *


if not (os.path.exists(".playlistGen.conf")):
    Redbold("/!\ Le fichier de configuration n'existe pas. Executez 'configure.py'. /!\\")
    sys.exit()
else:
    confFileName = ".playlistGen.conf"
    confFile = open(confFileName, 'r')

for ligne in confFile:
    if(ligne[0] != '#' and ligne[0] != '\n'):
        if(ligne.split("=")[0] == "LOGIN_BDD"):
            LOGIN_BDD = ligne.split("=")[1][:-1]
        if(ligne.split("=")[0] == "PASS_BDD"):
            PASS_BDD = ligne.split("=")[1][:-1]
        if(ligne.split("=")[0] == "DOMAIN_BDD"):
            DOMAIN_BDD = ligne.split("=")[1][:-1]
        if(ligne.split("=")[0] == "PORT_BDD"):
            PORT_BDD = ligne.split("=")[1][:-1]


ARGUMENTS_CLI = ['genre', 'sousgenre', 'artiste', 'album', 'titre']