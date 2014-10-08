#Import modules python
import argparse

argsParser = argparse.ArgumentParser()

#Déclaration des arguments positionnels
def defArgumentsPositionnels():
    argsParser.add_argument("duree_playlist", type=int, help="Durée totale de la playist en minutes")
    argsParser.add_argument("nom_playlist", help="Nom de sortie de la playist")
    argsParser.add_argument("type_playlist", help="Format de la playist", choices=['m3u', 'xspf', 'pls'])

#Déclaration des arguments optionnels
def defArgumentsOptionnels():
    argsParser.add_argument("-g", "--genre", action='append', nargs=2, help="")
    argsParser.add_argument("-G", "--sousgenre", action='append', nargs=2, help="")
    argsParser.add_argument("-a", "--artiste", action='append', nargs=2, help="")
    argsParser.add_argument("-A", "--album", action='append', nargs=2, help="")
    argsParser.add_argument("-t", "--titre", action='append', nargs=2, help="")
