# -*- coding: utf-8 -*-

"""Ce module permet d'établir la connexion à la base de données ainsi que la création de la table contenant les informations des morceaux"""

#Import modules Python
import sqlalchemy

#Import modules Projet
from globalConfig import LOGIN_BDD, PASS_BDD, DOMAIN_BDD, PORT_BDD

## Connexion à a base de donnée
connexionPG = sqlalchemy.create_engine("postgresql://"+ LOGIN_BDD +":"+ PASS_BDD +"@"+ DOMAIN_BDD +":"+ PORT_BDD +"/radio_libre")

## Meta-data de SQLAlchemy
metadata = sqlalchemy.MetaData()

## Table morceaux
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
