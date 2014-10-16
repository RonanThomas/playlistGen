# -*- coding: utf-8 -*-

confFileName = "playlistGen.conf"
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