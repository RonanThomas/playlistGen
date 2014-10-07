#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import logging

"""Vérification du pourcentage des arguments"""
def checkArgs(listeArguments, nomAttribut):
    global args
    try:
        i = 0
        for sous_liste in listeArguments:
            sous_liste[1] = int(sous_liste[1])
            if 0 < sous_liste[1] <= 100:
                listeArguments[i] = sous_liste
                setattr(args, nomAttribut, listeArguments)
                i += 1
            else:
                logging.error(str(sous_liste[1]) +  "n'est pas compris entre 0 et 100 !")
    except ValueError:
        logging.error(str(sous_liste[1]) + "n'est pas convertible en entier")
        
"""Calcul de la somme des pourcentage pour tous les arguments"""
def getSommePourcent():
    somme_pourcent = 0
    for attribut in ['genre','sousgenre','artiste','album','titre']:
        if getattr(args, attribut) is not None:
            for pourcentage in getattr(args, attribut):
                somme_pourcent += pourcentage[1]
    return somme_pourcent
                
parser = argparse.ArgumentParser()

"""Déclaration du fichier de logs"""
logging.basicConfig(filename="info.log", level=logging.DEBUG)

"""Déclaration des arguments positionnels"""
parser.add_argument("duree_playlist", type=int, help="Durée totale de la playist en minutes")
parser.add_argument("nom_playlist", help="Nom de sortie de la playist")
parser.add_argument("type_playlist", help="Format de la playist", choices=['m3u', 'xspf', 'pls'])

"""Déclaration des arguments optionnels"""
parser.add_argument("-g", "--genre", action='append', nargs=2, help="")
parser.add_argument("-G", "--sousgenre", action='append', nargs=2, help="")
parser.add_argument("-a", "--artiste", action='append', nargs=2, help="")
parser.add_argument("-A", "--album", action='append', nargs=2, help="")
parser.add_argument("-t", "--titre", action='append', nargs=2, help="")
args = parser.parse_args()

for attribut in ['genre','sousgenre','artiste','album','titre']:
    if getattr(args, attribut) is not None:
        checkArgs(getattr(args, attribut), attribut)
        
"""Vérification de la somme des pourcentage"""
if 0 < getSommePourcent() <= 100:
    
else:
    logging.error("Le pourcentage est supérieur à 100")
