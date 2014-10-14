#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import modules python
import logging
import time
import os
import sqlalchemy
import random

#Import modules projet
import verificationArguments
import definitionCLI
from globalConfig import ARGUMENTS_CLI
from connexion import connexionPG, metadata, tableMorceaux

#Déclaration du fichier de logs
logging.basicConfig(filename="info.log", level=logging.DEBUG)
logging.info("***** " + time.strftime('%d/%m/%y %H:%M:%S', time.localtime()) + " *****")

definitionCLI.defArgumentsPositionnels()
definitionCLI.defArgumentsOptionnels()

listeArgumentsCLI = definitionCLI.argsParser.parse_args()

for attribut in ARGUMENTS_CLI:
    if getattr(listeArgumentsCLI, attribut) is not None:
        verificationArguments.checkArgs(listeArgumentsCLI, getattr(listeArgumentsCLI, attribut), attribut)
        verificationArguments.checkSum(listeArgumentsCLI)

for attribut in ARGUMENTS_CLI:
    if getattr(listeArgumentsCLI, attribut) is not None:
        for argument in getattr(listeArgumentsCLI, attribut):
            selection_morceaux = sqlalchemy.select([tableMorceaux]).where(tableMorceaux.c.genre == argument[0])
            resultat = connexionPG.execute(selection_morceaux)
            resultat = list(resultat)
            argument.insert(2,[])
            i=0
            somme_duree = 0
            for ligne in resultat:
                somme_duree += ligne[5]
                if(somme_duree < argument[1]*60):
                    argument[2].insert(i, ligne)
                    i += 1
                else:
                    somme_duree -= ligne[5]
            
print(listeArgumentsCLI.genre)


def Redbold(output):
    os.system("tput bold")
    os.system("tput setaf 1")
    print(output)
    os.system("tput sgr 0")
    
def Bold(output):
    os.system("tput bold")
    print(output)
    os.system("tput sgr 0")
    
#for i in resultat:
#    Redbold("*****************************************************************")
#    Bold("Titre: " + i['titre'])
#    Bold("Genre: " + i['genre'])
#    Bold("Duree: " + str(i['duree']))
#    Bold("Chemin: " + i['chemin'])