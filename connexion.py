#Import modules Python
import sqlalchemy
from globalConfig import LOGIN_BDD, PASS_BDD, IP_BDD, PORT_BDD

#Connexion BDD
connexionPG = sqlalchemy.create_engine("postgresql://"+ LOGIN_BDD +":"+ PASS_BDD +"@"+ IP_BDD +":"+ PORT_BDD +"/radio_libre")
metadata = sqlalchemy.MetaData()

#Construction de la table morceaux
tableMorceaux = sqlalchemy.Table('morceaux', metadata,
                                 sqlalchemy.Column('titre', sqlalchemy.String),
                                 sqlalchemy.Column('album', sqlalchemy.String),
                                 sqlalchemy.Column('artiste', sqlalchemy.String),
                                 sqlalchemy.Column('genre', sqlalchemy.String),
                                 sqlalchemy.Column('sousgenre', sqlalchemy.String),
                                 sqlalchemy.Column('duree', sqlalchemy.Integer),
                                 sqlalchemy.Column('format', sqlalchemy.String),
                                 sqlalchemy.Column('polyphonie', sqlalchemy.Integer),
                                 sqlalchemy.Column('chemin', sqlalchemy.String))

#CHEMIN, TITRE, DUREE -> PLS
#CHEMIN -> XSPF / M3U