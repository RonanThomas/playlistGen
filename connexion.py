#Import modules Python
import sqlalchemy
from globalConfig import LOGIN_BDD, PASS_BDD, IP_BDD, PORT_BDD

#Connexion BDD
connexionPG = sqlalchemy.create_engine("postgresql://"+ LOGIN_BDD +":"+ PASS_BDD +"@"+ IP_BDD +":"+ PORT_BDD +"/radio_libre")
metadata = sqlalchemy.MetaData()

#Construction de la table morceaux
tableMorceaux = sqlalchemy.Table('morceaux', metadata, sqlalchemy.Column('titre', sqlalchemy.String))
