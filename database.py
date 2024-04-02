from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        # Chargement des données
        load_dotenv(encoding="utf-8")
        self.__host = os.getenv('host')
        self.__user = os.getenv('user')
        self.__password = os.getenv('passwd')
        self.__database = os.getenv('database')

    def __connect(self):
        '''
        connection to database
        '''
        mydb = mysql.connector.connect(

            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database,
            autocommit=True
        )
        cursor = mydb.cursor()
        return mydb, cursor

    def query(self, req, value, modif=False):
        mydb, cursor = self.__connect()
        try:
            # Envoie la requete ("req") à la base de donnée
            cursor.execute(req, value)
            # Par défault il fait un fetchall et il retourne le resultat
            if modif is False:
                result = cursor.fetchall()
                return result

        except Error as e:
            # Annule les modif effectuées
            mydb.rollback()
            print(e)

    def close(self):
        self.cursor.close()
        self.mydb.close()


if __name__ == "__main__":
    gestion = Database()
