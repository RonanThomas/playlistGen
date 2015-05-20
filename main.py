#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import modules Python
import logging
import time

#Import modules Projet
import verificationArguments
import definitionCLI
from globalConfig import ARGUMENTS_CLI
from genPlaylist import downloadData, genPlaylist, writeFile, playlist
from writeLogFile import writeLogs
from color import Red, Redbold, Bold

#Déclaration du fichier de logs
logging.basicConfig(filename="info.log", level=logging.DEBUG, format="")
logging.info("*********************************")
logging.info("******* " + time.strftime('%d/%m/%y %H:%M:%S', time.localtime()) + " *******\n")

Redbold("Génération de la playslit...")

#Déclaration de la ligne de commande
definitionCLI.defArgumentsPositionnels()
definitionCLI.defArgumentsOptionnels()

Bold("Parcours de ligne de commande...")
## Déclaration du parser
listeArgumentsCLI = definitionCLI.argsParser.parse_args()

Bold("Vérification des arguments...")
#Vérification de la somme des pourcentage pour tous les arguments
for attribut in ARGUMENTS_CLI:
    if getattr(listeArgumentsCLI, attribut) is not None:
        verificationArguments.checkSum(listeArgumentsCLI)
        
Bold("Sélection des morceaux...")
#Téléchargement des données
downloadData(listeArgumentsCLI)
#Génération de la playlist
Bold("Génération de la playlist...")
## Durée exacte de la playlist
somme_duree = genPlaylist(listeArgumentsCLI)
Bold("Génération terminée !")
Bold("Ecriture du fichier de playlist...")
#Ecriture du fichier de playlist
writeFile(listeArgumentsCLI, playlist)
Bold("Ecriture du fichier de logs...")
#Ecriture du fichier de log
writeLogs(listeArgumentsCLI, playlist, somme_duree)
Redbold("Playlist enregistrée en tant '"+ listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist +"'")
