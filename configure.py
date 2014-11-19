#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import modules Python
import getpass
import argparse
import sys

#Import modules Projet
from configuration import writeConfig
from color import Red, Redbold, Bold

def saisiePassword():
    while True:
        pass_bdd = getpass.getpass("Saisir le mot de passe de la base de données : ")
        confirm_pass_bdd = getpass.getpass("Confirmation du mot de passe de la base de données : ")
        if pass_bdd == confirm_pass_bdd:
            break
        else:
            Red("/!\ Les mots de passe sont différents /!\\")
    return pass_bdd

argsParser = argparse.ArgumentParser()
login_bdd = pass_bdd = domain_bdd = port_bdd = None
configFileName = ".playlistGen.conf"

argsParser.add_argument("-l", "--login", help="Modification du LOGGIN")
argsParser.add_argument("-d", "--domain", help="Modification du DOMAIN")
argsParser.add_argument("-p", "--port", help="Modification du PORT")

listeArgumentsCLI = argsParser.parse_args()
    
Redbold("Configuration de playlistGen...")

if not (listeArgumentsCLI.login is None and listeArgumentsCLI.domain == None and listeArgumentsCLI.port == None):
    configFile = open(".playlistGen.conf", 'r')
    for ligne in configFile:
        if(ligne.split('=')[0] == 'LOGIN_BDD'):
            login_bdd = ligne.split('=')[1][:-1]
        if(ligne.split('=')[0] == 'PASS_BDD'):
            pass_bdd = ligne.split('=')[1][:-1]
        if(ligne.split('=')[0] == 'DOMAIN_BDD'):
            domain_bdd = ligne.split('=')[1][:-1]
        if(ligne.split('=')[0] == 'PORT_BDD'):
            port_bdd = ligne.split('=')[1][:-1]
    
    if(login_bdd is None or pass_bdd is None or domain_bdd is None or port_bdd is None):
        Redbold("/!\ Le fichier de configuration n'est pas complet. Executez 'configure.py'. /!\\")
        sys.exit()
    
configFile = open(configFileName, 'w')
writeConfig.writeHead(configFile)

if(listeArgumentsCLI.login is None and listeArgumentsCLI.domain is None and listeArgumentsCLI.port is None):
    login_bdd = input("Saisir l'identifiant de la base de données : ")
    pass_bdd = saisiePassword()
    domain_bdd = input("Saisir le domaine ou l'IP du SGBD : ")
    
    while True:
        port_bdd = input("Saisir le port du SGBD : ")
        try:
            port_bdd = abs(int(port_bdd))
            if(port_bdd > 0 and port_bdd <= 65535):
                break
            else:
                Red("/!\ Le numéro du port doit être compris entre 1 et 65535 /!\\")
        except ValueError:
            Red("/!\ Le numéro du port saisie n'est pas un nombre (NaN): '" + port_bdd + "' /!\\")
    
    writeConfig.writeData(configFile, login_bdd, pass_bdd, domain_bdd, port_bdd)

else:
    if listeArgumentsCLI.login is not None:
        Bold("Modification du LOGIN")
        login_bdd = listeArgumentsCLI.login
            
    if listeArgumentsCLI.domain is not None:
        Bold("Modification du DOMAIN")
        domain_bdd = listeArgumentsCLI.domain
        
    if listeArgumentsCLI.port is not None:
        try:
            port_bdd = abs(int(listeArgumentsCLI.port))
            if(port_bdd > 0 and port_bdd <= 65535):
                Bold("Modification du PORT")
                port_bdd = listeArgumentsCLI.port
            else:
                Red("/!\ Le numéro du port doit être compris entre 1 et 65535 /!\\")
                sys.exit()
        except ValueError:
            Red("/!\ Le numéro du port saisie n'est pas un nombre (NaN): '" + listeArgumentsCLI.port + "' /!\\")
            sys.exit()
    
    writeConfig.writeData(configFile, login_bdd, domain_bdd, port_bdd)
            
Redbold("Configuration de playlistGen terminée.")
