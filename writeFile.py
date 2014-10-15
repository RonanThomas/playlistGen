from globalConfig import ARGUMENTS_CLI
import os

def writeM3U(listeArgumentsCLI, playlist):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    for musique in playlist:
        playlistFile.write(musique[2] + "\n")
    playlistFile.close()
    

def writeXSPF(listeArgumentsCLI, playlist):
    pass

def writePLS(listeArgumentsCLI, playlist):
    pass
