# -*- coding: utf-8 -*-

#Import modules Python
import logging
import calcul

'''Vérification de la somme des pourcentages'''    
def checkSum(listeArgumentsCLI):
    if 0 < calcul.getSommePourcent(listeArgumentsCLI) <= 100:
        calcul.convertToMinute(listeArgumentsCLI)
    else:
        logging.error("La somme des pourcentage est supérière à 100%")
