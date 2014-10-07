#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import logging

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
                
parser = argparse.ArgumentParser()

logging.basicConfig(filename="info.log", level=logging.DEBUG)


parser.add_argument("duree_playlist", type=int, help="Durée totale de la playist en minutes")
parser.add_argument("nom_playlist", help="Nom de sortie de la playist")
parser.add_argument("type_playlist", help="Format de la playist", choices=['m3u', 'xspf', 'pls'])
parser.add_argument("-g", "--genre", action='append', nargs=2, help="")
parser.add_argument("-G", "--sousgenre", action='append', nargs=2, help="")
parser.add_argument("-a", "--artiste", action='append', nargs=2, help="")
parser.add_argument("-A", "--album", action='append', nargs=2, help="")
parser.add_argument("-t", "--titre", action='append', nargs=2, help="")
args = parser.parse_args()

for attribut in ['genre','sousgenre','artiste','album','titre']:
    if getattr(args, attribut) is not None:
        checkArgs(getattr(args, attribut), attribut)
