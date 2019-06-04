import csv
import logging
import sqlparse
import mysql.connector
from mysql.connector import errorcode

class Database(object):
    log = logging.getLogger("DATABASE_SERVICE")
    cards_file = '../database/mysql/conf.d/00_cards.sql'

    def __init__(self):
        self.log.info("Establishing database connection.")
        try:
            self.cnx = mysql.connector.connect(user='local', password='local', host='192.168.33.10', database='pick1')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.log.critical("Something is wrong with you user name or password")
                exit(-1)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.log.critical("Database does not exist.")

    def __del__(self):
        self.log.info("Closing database connection.")
        self.cnx.close()

    def count(self, set):
        cursor = self.cnx.cursor()
        query = "SELECT COUNT(*) FROM cards WHERE set_code = '" + set.code + "';"
        cursor.execute(query)
        return cursor.fetchone()[0]

    def add(self, card):
        cursor = self.cnx.cursor()
        query = "INSERT INTO cards (name, set_code, image_uri, picks, appearances, layout) \n" \
                "SELECT '" + card.escaped_name() + "', '" + card.set_code + "', '" + card.slug() + "', " \
                "0, 0, '" + card.layout + "' \n" + "WHERE NOT EXISTS \n" + "(SELECT id FROM "  \
                "cards WHERE name = '" + card.escaped_name() + "' AND set_code = '" + card.set_code +"' "\
                "AND image_uri = '" + card.slug() + "' AND layout = '" + card.layout + "')"
        cursor.execute(query)
        self.cnx.commit()

    
