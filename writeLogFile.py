# -*- coding: utf-8 -*-

#Import modules Python
import logging

def writeLogs(listeArgumentsCLI, playlist, somme_duree):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    logging.info("Nom de la playlist : " + playlistFileName + "\n")
    
    nombrePiste = len(playlist)
    logging.info("Nombre de pistes : " + str(nombrePiste) + "\n")
    
    logging.info("Durée totale : " + convertToHours(somme_duree) + "\n\n")
    
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
            heures = heures % 60
        
    return str(jours) + "j " + str(heures) + "h " + str(minutes) + "m " + str(secondes) + "s"