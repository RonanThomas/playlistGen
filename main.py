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

definitionCLI.defArgumentsPositionnels()
definitionCLI.defArgumentsOptionnels()

listeArgumentsCLI = definitionCLI.argsParser.parse_args()

for attribut in ARGUMENTS_CLI:
    if getattr(listeArgumentsCLI, attribut) is not None:
        verificationArguments.checkSum(listeArgumentsCLI)

downloadData(listeArgumentsCLI)
genPlaylist(listeArgumentsCLI)