# -*- coding: utf-8 -*-

#Import modules Python
import argparse
import logging
import sys

'''Classe de vérification des arguments'''
class appendCheckArgs(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs == 2:
            super(appendCheckArgs, self).__init__(option_strings, dest, nargs=nargs, **kwargs)
        else:
            logging.error("Option %s nécéssite deux arguments" % option_strings)
    
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            quantity = abs(int(values[1]))
            values[1] = quantity if 100 >= quantity > 0 else None
        except ValueError:
            logging.error("La qantité saisie n'est pas un nombre (NaN): '" + values[1] + "'")
            sys.exit(1)
        current_dest_value = getattr(namespace, self.dest)
        if type(current_dest_value) is list:
            current_dest_value.append(values)
            setattr(namespace, self.dest, current_dest_value)
        else:
            logging.debug(values)
            setattr(namespace, self.dest, [values])

argsParser = argparse.ArgumentParser()

'''"Déclaration des arguments positionnels'''
def defArgumentsPositionnels():
    argsParser.add_argument("duree_playlist", type=int, help="Durée totale de la playist en minutes")
    argsParser.add_argument("nom_playlist", help="Nom de sortie de la playist")
    argsParser.add_argument("type_playlist", help="Format de la playist", choices=['m3u', 'xspf', 'pls'])

'''Déclaration des arguments optionnels'''
def defArgumentsOptionnels():
    argsParser.add_argument("-g", "--genre", action=appendCheckArgs, nargs=2, help="")
    argsParser.add_argument("-G", "--sousgenre", action=appendCheckArgs, nargs=2, help="")
    argsParser.add_argument("-a", "--artiste", action=appendCheckArgs, nargs=2, help="")
    argsParser.add_argument("-A", "--album", action=appendCheckArgs, nargs=2, help="")
    argsParser.add_argument("-t", "--titre", action=appendCheckArgs, nargs=2, help="")
