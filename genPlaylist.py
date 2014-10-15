# -*- coding: utf-8 -*-

#Import modules python
import sqlalchemy
import random

#Import modules projet
from globalConfig import ARGUMENTS_CLI
from connexion import connexionPG, tableMorceaux
from writeFile import writeM3U, writeXSPF, writePLS

def downloadData(listeArgumentsCLI):
    global resultat
    for attribut in ARGUMENTS_CLI:
        if getattr(listeArgumentsCLI, attribut) is not None:
            for argument in getattr(listeArgumentsCLI, attribut):
                if(attribut == 'genre'):
                    selection_morceaux = sqlalchemy.select([tableMorceaux]).where(tableMorceaux.c.genre == argument[0])
                if(attribut == 'sousgenre'):
                    selection_morceaux = sqlalchemy.select([tableMorceaux]).where(tableMorceaux.c.sousgenre == argument[0])
                if(attribut == 'artiste'):
                    selection_morceaux = sqlalchemy.select([tableMorceaux]).where(tableMorceaux.c.artiste == argument[0])
                if(attribut == 'album'):
                    selection_morceaux = sqlalchemy.select([tableMorceaux]).where(tableMorceaux.c.album == argument[0])
                if(attribut == 'titre'):
                    selection_morceaux = sqlalchemy.select([tableMorceaux]).where(tableMorceaux.c.titre == argument[0])
                
                resultat = connexionPG.execute(selection_morceaux)
                resultat = list(resultat)
                random.shuffle(resultat)
    
    saveData(listeArgumentsCLI)
                
def saveData(listeArgumentsCLI):
    for attribut in ARGUMENTS_CLI:
        if getattr(listeArgumentsCLI, attribut) is not None:
            for argument in getattr(listeArgumentsCLI, attribut):
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

def genPlaylist(listeArgumentsCLI):
    playlist = []
    i = 0
    for attribut in ARGUMENTS_CLI:
        if getattr(listeArgumentsCLI, attribut) is not None:
            for argument in getattr(listeArgumentsCLI, attribut):
                for musique in argument[2]:
                    playlist.insert(i, [musique[0], musique[5], musique[8]])
                    i += 1
    random.shuffle(playlist)
    
    writeFile(listeArgumentsCLI, playlist)

def writeFile(listeArgumentsCLI, playlist):
    if(listeArgumentsCLI.type_playlist == 'm3u'):
        writeM3U(listeArgumentsCLI, playlist)
    if(listeArgumentsCLI.type_playlist == 'xspf'):
        writeXSPF(listeArgumentsCLI, playlist)
    if(listeArgumentsCLI.type_playlist == 'pls'):
        writePLS(listeArgumentsCLI, playlist)