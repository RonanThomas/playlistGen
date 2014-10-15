from globalConfig import ARGUMENTS_CLI
import os

def writeM3U(listeArgumentsCLI, playlist):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    for musique in playlist:
        playlistFile.write(musique[2] + "\n")
    playlistFile.close()
    

def writeXSPF(listeArgumentsCLI, playlist):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    playlistFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n\t<trackList>")
    for musique in playlist:
        playlistFile.write("<track><location>"+ musique[2] +"</location></track>")
    playlistFile.write("\t</trackList>\n</playlist>")
    playlistFile.close()

def writePLS(listeArgumentsCLI, playlist):
    i=1
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    playlistFile.write("[playlist]\n")
    for musique in playlist:
        playlistFile.write("File"+ i +"="+ musique[2] +"\nTitle" + i +"="+ musique[0] +"\nLength"+ i +"="+ musique[1])
        i+=1
    playlistFile.write("NumberOfEntries="+ playlist.size() +"\nVersion=2")
    playlistFile.close()