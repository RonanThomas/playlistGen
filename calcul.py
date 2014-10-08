#Import modules projet
import main

#Calcul de la somme des pourcentage pour tous les arguments
def getSommePourcent():
    somme_pourcent = 0
    for attribut in ['genre','sousgenre','artiste','album','titre']:
        if getattr(main.listeArgumentsCLI, attribut) is not None:
            for pourcentage in getattr(main.listeArgumentsCLI, attribut):
                somme_pourcent += pourcentage[1]
    return somme_pourcent

#Conversion des pourcentages en minutes
def convertToMinute():
    for attribut in ['genre','sousgenre','artiste','album','titre']:
        if getattr(main.listeArgumentsCLI, attribut) is not None:
            for argument in getattr(main.listeArgumentsCLI, attribut):
                argument[1] = int(main.listeArgumentsCLI.duree_playlist*argument[1]/100)
