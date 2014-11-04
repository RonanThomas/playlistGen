# -*- coding: utf-8 -*-

'''Ecriture du fichier de playlist au format M3U'''
def writeM3U(listeArgumentsCLI, playlist):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    for musique in playlist:
        playlistFile.write(musique[5] + "\n")
    playlistFile.close()

'''Ecriture du fichier de playlist au format XSPF'''
def writeXSPF(listeArgumentsCLI, playlist):
    playlistFileName = listeArgumentsCLI.nom_playlist +"."+ listeArgumentsCLI.type_playlist
    playlistFile = open(playlistFileName, 'w')
    playlistFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "\t<title>"+ playlistFileName +"</title>\n"+
                       "\t<trackList>\n")
    for musique in playlist:
        playlistFile.write("\t\t<track>\n\t\t\t<location>"+ musique[5] +"</location>\n"+
                           "\t\t\t<title>"+ musique[0] +"</title>\n"+
                           "\t\t\t<creator>"+ musique[1] +"</creator>\n"+
                           "\t\t\t<album>"+ musique[2] +"</album>\n"+
                           "\t\t\t<genre>"+ musique[3] +"</genre>\n"+
                           "\t\t\t<duration>"+ str(musique[4] * 1000) +"</duration>\n"+
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
        playlistFile.write("File"+ str(i) +"="+ musique[4] +"\nTitle" + str(i) +"="+ musique[0] +"\nLength"+ str(i) +"="+ str(musique[3]) +"\n")
        i+=1
    playlistFile.write("NumberOfEntries="+ str(len(playlist)) +"\nVersion=2")
    playlistFile.close()
