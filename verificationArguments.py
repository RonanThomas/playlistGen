#Import modules projet
import main
import calcul

"""Vérification du pourcentage des arguments"""
def checkArgs(listeArguments, nomAttribut):
    global args
    try:
        i = 0
        for sublisteArguments in listeArguments:
            sublisteArguments[1] = int(sublisteArguments[1])
            if 0 < sublisteArguments[1] <= 100:
                listeArguments[i] = sublisteArguments
                setattr(main.listeArgumentsCLI, nomAttribut, listeArguments)
                i += 1
            else:
                main.logging.error(str(sublisteArguments[1]) +  "n'est pas compris entre 0 et 100 !")
    except ValueError:
        main.logging.error(str(sublisteArguments[1]) + "n'est pas convertible en entier")

"""Vérification de la somme des pourcentage"""    
def blabla():
    if 0 < calcul.getSommePourcent() <= 100:
        calcul.convertToMinute()
        for attribut in ['genre','sousgenre','artiste','album','titre']:
            if getattr(main.listeArgumentsCLI, attribut) is not None:
                for argument in getattr(main.listeArgumentsCLI, attribut):
                    main.logging.info(attribut + "\t" + argument[0] + ", " + str(argument[1]) + " minutes")
            else:
                main.logging.error("Le pourcentage est supérieur à 100%")
