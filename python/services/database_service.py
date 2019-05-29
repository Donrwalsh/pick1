import csv
import logging
import sqlparse
import mysql.connector
from mysql.connector import errorcode

class Database(object):
    log = logging.getLogger("DATABASE_SERVICE")
    cards_file = '../database/mysql/conf.d/00_cards.sql'

    def __init__(self):
        print("hello there")

    def verify_connection(self):
        try:
            cnx = mysql.connector.connect(user='local', password='local', host='192.168.33.10', database='pick1')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.log.critical("Something is wrong with you user name or password")
                exit(-1)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.log.critical("Database does not exist.")

    def function(self):
        cnx = mysql.connector.connect(user='local', password='local', host='192.168.33.10', database='pick1')
        cursor = cnx.cursor()
        query = "SELECT * FROM cards;"
        cursor.execute(query)
        for result in cursor:
            print(result)
        cnx.close()

    
