#Import modules projet
import logging
import calcul

"""Vérification du pourcentage des arguments"""
def checkArgs(listeArgumentsCLI, listeArguments, nomAttribut):
    try:
        i = 0
        for sublisteArguments in listeArguments:
            sublisteArguments[1] = int(sublisteArguments[1])
            if 0 < sublisteArguments[1] <= 100:
                listeArguments[i] = sublisteArguments
                setattr(listeArgumentsCLI, nomAttribut, listeArguments)
                i += 1
            else:
                logging.error(str(sublisteArguments[1]) +  "n'est pas compris entre 0 et 100 !")
    except ValueError:
        logging.error(str(sublisteArguments[1]) + "n'est pas convertible en entier")

"""Vérification de la somme des pourcentages"""    
def checkSum(listeArgumentsCLI):
    if 0 < calcul.getSommePourcent(listeArgumentsCLI) <= 100:
        calcul.convertToMinute(listeArgumentsCLI)
    else:
        logging.error("La somme des pourcentage est supérière à 100%")
