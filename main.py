#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import modules Python
import logging
import time

#Import modules Projet
import verificationArguments
import definitionCLI
from globalConfig import ARGUMENTS_CLI
from genPlaylist import downloadData, genPlaylist

#Déclaration du fichier de logs
logging.basicConfig(filename="info.log", level=logging.DEBUG)
logging.info("***** " + time.strftime('%d/%m/%y %H:%M:%S', time.localtime()) + " *****")

#Déclaration de la ligne de commande
definitionCLI.defArgumentsPositionnels()
definitionCLI.defArgumentsOptionnels()

#Déclaration du parser
listeArgumentsCLI = definitionCLI.argsParser.parse_args()

#Vérification de la somme des pourcentage pour tous les arguments
for attribut in ARGUMENTS_CLI:
    if getattr(listeArgumentsCLI, attribut) is not None:
        verificationArguments.checkSum(listeArgumentsCLI)

#Téléchargement des données
downloadData(listeArgumentsCLI)
#Génération de la playlist
genPlaylist(listeArgumentsCLI)