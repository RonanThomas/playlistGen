# -*- coding: utf-8 -*-

'''Ecriture du fichier de playlist au format M3U'''
def writeM3U(listeArgumentsCLI, playlist):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    for musique in playlist:
        playlistFile.write(musique[4] + "\n")
    playlistFile.close()

'''Ecriture du fichier de playlist au format XSPF'''
def writeXSPF(listeArgumentsCLI, playlist):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    playlistFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "<title>"+ playlistFileName +"</title>"+
                       "\t<trackList>\n")
    for musique in playlist:
        playlistFile.write("\t\t<track>\n\t\t\t<location>"+ musique[4] +"</location>\n"+
                           "\t\t\t<title>"+ musique[0] +"</title>\n"+
                           "\t\t\t<creator>"+ musique[1] +"</creator>\n"+
                           "\t\t\t<album>"+ musique[2] +"</album>\n"+
                           "\t\t\t<duration>"+ str(musique[3] * 1000) +"</duration>\n"+
                           "\t\t</track>\n")
    playlistFile.write("\t</trackList>\n</playlist>")
    playlistFile.close()

'''Ecriture du fichier de playlist au format PLS'''
def writePLS(listeArgumentsCLI, playlist):
    i=1
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    playlistFile.write("[playlist]\n")
    for musique in playlist:
        playlistFile.write("File"+ i +"="+ musique[4] +"\nTitle" + i +"="+ musique[0] +"\nLength"+ i +"="+ musique[3])
        i+=1
    playlistFile.write("NumberOfEntries="+ playlist.size() +"\nVersion=2")
    playlistFile.close()
