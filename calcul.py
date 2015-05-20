# -*- coding: utf-8 -*-

#Import modules Projet
from globalConfig import ARGUMENTS_CLI

## Calcul de la somme des pourcentages pour tous les arguments
#  @param listeArgumentsCLI : Namespace
#  @return somme_pourcent : Int
def getSommePourcent(listeArgumentsCLI):
    somme_pourcent = 0
    for attribut in ARGUMENTS_CLI:
        if getattr(listeArgumentsCLI, attribut) is not None:
            for pourcentage in getattr(listeArgumentsCLI, attribut):
                somme_pourcent += pourcentage[1]
    return somme_pourcent


## Convertie les pourcentage en minutes selon la durée totale de la plyalist
#  @param listeArgumentsCLI : Namespace
#  @return listeArgumentsCLI : Namespace
def convertToMinute(listeArgumentsCLI):
    for attribut in ARGUMENTS_CLI:
        if getattr(listeArgumentsCLI, attribut) is not None:
            for argument in getattr(listeArgumentsCLI, attribut):
                argument[1] = int(listeArgumentsCLI.duree_playlist*argument[1]/100)
