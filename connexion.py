#Import module Python
import sqlalchemy
from identifiant import loginBDD, passwordBDD, ipBDD, portBDD

#Connexion a la BDD
connexion = sqlalchemy.create_engine("postgresql://"+ loginBDD +":"+ passwordBDD +"@"+ ipBDD +":"+ portBDD +"/radio_libre")

metadata = sqlalchemy.MetaData()

#Construction de la table morceaux
tableMorceaux = sqlalchemy.Table('morceaux', metadata, sqlalchemy.Column('titre', sqlalchemy.String))

#Selection des des valeurs trouvées sur la BDD
selection = sqlalchemy.select([tableMorceaux])

#Execution de la requete
morceaux = connexion.execute(selection)

#Affichage des valeurs trouvées
for i in morceaux:
    print(i)