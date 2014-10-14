#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import modules python
import logging
import time

#Import modules projet
import verificationArguments
import definitionCLI
from globalConfig import ARGUMENTS_CLI

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