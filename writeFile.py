from globalConfig import ARGUMENTS_CLI
import os

def writeM3U(listeArgumentsCLI, playlist):
    playlistFile = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    file = open(playlistFile,'w')
    for musique in playlist:
        file.write(musique[2] + "\n")
    file.close()
    

def writeXSPF(listeArgumentsCLI, playlist):
    pass

def writePLS(listeArgumentsCLI, playlist):
    pass