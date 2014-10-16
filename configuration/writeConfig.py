# -*- coding: utf-8 -*-

def writeHead(configFile):
    configFile.write("#######################################################################\n")
    configFile.write("#\n")
    configFile.write("# Fichier de configuration de 'playlistGen'\n")
    configFile.write("# LOGIN_BDD correspond à l'identifiant de la base de donnée\n")
    configFile.write("# PASS_BDD correspond au mot de passe de la base de donnée\n")
    configFile.write("# DOMAIN_BDD correspond au nom de domaine ou l'adresse IP du SGBD\n")
    configFile.write("# PORT_BDD correspond au port d'écoute du SGBD\n")
    configFile.write("#\n")
    configFile.write("#######################################################################\n")
    configFile.write("#\n")
    configFile.write("# /!\     NE JAMAIS MODIFIER LES VALEURS DU FICHIER     /!\\\n")
    configFile.write("# /!\ UTILISEZ 'configure.py' POUR MODIFIER LES VALEURS /!\\\n")
    configFile.write("#\n")
    configFile.write("#######################################################################\n\n")
    
def writeData(configFile, login_bdd, pass_bdd, domain_bdd, port_bdd):
    configFile.write("LOGIN_BDD="+ login_bdd +"\n")
    configFile.write("PASS_BDD="+ pass_bdd +"\n")
    configFile.write("DOMAIN_BDD="+ domain_bdd +"\n")
    configFile.write("PORT_BDD="+ str(port_bdd) +"\n\n")
    configFile.write("#######################################################################\n")