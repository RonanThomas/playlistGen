# -*- coding: utf-8 -*-

#Import modules Python
import sqlalchemy
import random

#Import modules Projet
from globalConfig import ARGUMENTS_CLI
from connexion import connexionPG, tableMorceaux
from writeFile import writeM3U, writeXSPF, writePLS

'''Téléchargement des données de la base de données'''
def downloadData(listeArgumentsCLI):
    print("DownloadData")
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


'''Génération de la liste de playlist'''
def genPlaylist(listeArgumentsCLI):
    print("genPlaylist")
    playlist = []
    i = 0
    for attribut in ARGUMENTS_CLI:
        if getattr(listeArgumentsCLI, attribut) is not None:
            for argument in getattr(listeArgumentsCLI, attribut):
                for musique in argument[2]:
                    playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
                    i += 1
    random.shuffle(playlist)
    
    completePlaylist(listeArgumentsCLI, playlist)
    

def completePlaylist(listeArgumentsCLI, playlist):
    somme_duree = 0
    for musique in playlist:
        somme_duree += musique[5]
    
    print("somme_duree: "+somme_duree)
    if(somme_duree < listeArgumentsCLI.duree_playlist*60):
        selection_morceaux = sqlalchemy.select([tableMorceaux])
        resultat = connexionPG.execute(selection_morceaux)
        resultat = list(resultat)
        random.shuffle(resultat)
    
    i=len(playlist)
    print(str(i) )
    for musique in resultat:
        somme_duree += musique[5]
        if(somme_duree < listeArgumentsCLI.duree_playlist*60):
            playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
            i += 1
        else:
            somme_duree -= musique[5]
    
    writeFile(listeArgumentsCLI, playlist)
    
    
'''Appel de la fonction d'écriture du fichir de playlist'''
def writeFile(listeArgumentsCLI, playlist):
    print("writeFile")
    if(listeArgumentsCLI.type_playlist == 'm3u'):
        writeM3U(listeArgumentsCLI, playlist)
    if(listeArgumentsCLI.type_playlist == 'xspf'):
        writeXSPF(listeArgumentsCLI, playlist)
    if(listeArgumentsCLI.type_playlist == 'pls'):
        writePLS(listeArgumentsCLI, playlist)
