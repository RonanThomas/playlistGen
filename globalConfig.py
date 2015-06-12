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
    ## Chemin du fichier de configuration
    confFileName = ".playlistGen.conf"

    ## Fichier de configuration
    confFile = open(confFileName, 'r')

for ligne in confFile:
    if(ligne[0] != '#' and ligne[0] != '\n'):
        if(ligne.split("=")[0] == "LOGIN_BDD"):
            ## Identifiant de la base de données
            LOGIN_BDD = ligne.split("=")[1][:-1]
        if(ligne.split("=")[0] == "PASS_BDD"):
            ## Mot de passe de la base de données
            PASS_BDD = ligne.split("=")[1][:-1]
        if(ligne.split("=")[0] == "DOMAIN_BDD"):
            ## Hôte du serveur de base de données
            DOMAIN_BDD = ligne.split("=")[1][:-1]
        if(ligne.split("=")[0] == "PORT_BDD"):
            ## Port du serveur de base de données
            PORT_BDD = ligne.split("=")[1][:-1]


ARGUMENTS_CLI = ['genre', 'sousgenre', 'artiste', 'artisteRegex', 'album', 'titre']
