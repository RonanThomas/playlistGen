#Import modules Python
import sqlalchemy
from accessBDD import loginBDD, passwordBDD, ipBDD, portBDD

#Connexion BDD
connexionPG = sqlalchemy.create_engine("postgresql://"+ loginBDD +":"+ passwordBDD +"@"+ ipBDD +":"+ portBDD +"/radio_libre")
metadata = sqlalchemy.MetaData()

#Construction de la table morceaux
tableMorceaux = sqlalchemy.Table('morceaux', metadata, sqlalchemy.Column('titre', sqlalchemy.String))
