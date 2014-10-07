#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import logging

def checkArgs(arg):
    try:
        int(arg[1])
        if int(arg[1]) > 0 and int(arg[1]) <= 100:
            return int(arg[1])
        else:
            logging.error(arg[1] +  "n'est pas compris entre 0 et 100 !")
    except ValueError:
        logging.error(arg[1] + "n'est pas convertible en entier")
                
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

if args.genre:
    for arg in args.genre:
        checkArgs(arg)
        print(args.genre)
if args.artiste:
    for arg in args.artiste:
        checkArgs(args.artiste)
        print(args.genre)
