# -*- coding: utf-8 -*-

#Import modules Python
import logging

## Ecriture du fichier du fichier de logs
#  @param listeArgumentsCLI : Namespace
#  @param playlist : List
#  @param somme_duree : Int
def writeLogs(listeArgumentsCLI, playlist, somme_duree):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    logging.info("Nom de la playlist : " + playlistFileName + "\n")
    
    nombrePiste = len(playlist)
    logging.info("Nombre de pistes : " + str(nombrePiste) + "\n")
    
    logging.info("Durée totale : " + convertToHours(somme_duree))
    logging.info("Pourcentage manquant : " + str((((listeArgumentsCLI.duree_playlist * 60)-somme_duree)/(listeArgumentsCLI.duree_playlist * 60))*100)[:5] + "%\n\n")
    

## Convertie en heure/minutes/secondes un durée en minutes
#  @param duree : Int
def convertToHours(duree):
    jours = 0
    heures = 0
    
    secondes = duree % 60
    minutes = int(duree / 60)
    if(duree >= 3600):
        heures = int(minutes / 60)
        minutes = minutes % 60
        if(duree >= 86400):
            jours = int(heures / 24)
            heures = heures % 24
        
    return str(jours) + "j " + str(heures) + "h " + str(minutes) + "m " + str(secondes) + "s"
