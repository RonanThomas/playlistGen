# -*- coding: utf-8 -*-

#Import modules Python
import sqlalchemy
import random

#Import modules Projet
import calcul
from globalConfig import ARGUMENTS_CLI
from connexion import connexionPG, tableMorceaux
from writePlaylistFile import writeM3U, writeXSPF, writePLS
from color import Red, Redbold, Bold

playlist = []

## Téléchargement des données de la base de données
#  @param listeArgumentsCLI : Namespace
#  @return listeArgumentsCLI : Namespace
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


## Génération de la liste de playlist
#  @param listeArgumentsCLI : Namespace
#  @return completePlaylist(listeArgumentsCLI) : Int
def genPlaylist(listeArgumentsCLI):
    i = 0
    for attribut in ARGUMENTS_CLI:
        if getattr(listeArgumentsCLI, attribut) is not None:
            for argument in getattr(listeArgumentsCLI, attribut):
                for musique in argument[2]:
                    playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
                    i += 1
    random.shuffle(playlist)
    
    if(calcul.getSommePourcent(listeArgumentsCLI) != 100):
        return completePlaylist(listeArgumentsCLI)
    
## Completion de la playlist par des titres aléatoires
#  @param listeArgumentsCLI : Namespace
#  @return somme_duree : Int
def completePlaylist(listeArgumentsCLI):
    somme_duree = 0
    for musique in playlist:
        somme_duree += musique[3]
    
    if(somme_duree < listeArgumentsCLI.duree_playlist*60):
        selection_morceaux = sqlalchemy.select([tableMorceaux])
        resultat = connexionPG.execute(selection_morceaux)
        resultat = list(resultat)
        random.shuffle(resultat)
    
    i=len(playlist)
    for musique in resultat:
        somme_duree += musique[5]
        if(somme_duree < listeArgumentsCLI.duree_playlist*60):
            playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
            i += 1
        else:
            somme_duree -= musique[5]
            
    return somme_duree


## Appel de la fonction d'écriture du fichir de playlist
#  @param listeArgumentsCLI : Namespace
#  @param playlist : List
def writeFile(listeArgumentsCLI, playlist):
    if(listeArgumentsCLI.type_playlist == 'm3u'):
        writeM3U(listeArgumentsCLI, playlist)
    if(listeArgumentsCLI.type_playlist == 'xspf'):
        writeXSPF(listeArgumentsCLI, playlist)
    if(listeArgumentsCLI.type_playlist == 'pls'):
        writePLS(listeArgumentsCLI, playlist)
