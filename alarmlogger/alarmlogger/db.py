import sqlite3
import os
# from datetime import datetime
from dateutil import parser

SCHEMA_VERSION = 1

class Db(object):
    def __init__(self):
        """
        Lets get started.
        
        :param db_file: 
        """
        self.db_file = os.environ['AVOBROKER_DB_FILE']
        self.conn = get_db_conn(os.environ['AVOBROKER_DB_FILE'])

    def insert_alarm(self, alarm):
        """
        
        :param alarm: 
        :return: 
        """

        sql = '''INSERT INTO alarm (volcano, subject, message) 
                VALUES (?, ?, ?)'''
        q = self.conn.execute(sql, (alarm['volcano'], alarm['subject'], alarm['message']))

        self.conn.commit()

    def count_alarms(self):
        """
        
        :param: 
        :return:  Count of alarms
        """

        sql = 'SELECT count(*) FROM alarm'
        q = self.conn.execute(sql)
        count = q.fetchone()[0]

        return count


    def get_alarms(self):
        sql = 'SELECT volcano, subject, message FROM alarm'

        alarms = []
        q = self.conn.execute(sql)
        for row in q:
            alarms.append({
                'volcano': row[0],
                'subject': row[1],
                'message': row[2].replace('\n', '<br />')
            })
        return alarms

    def close(self):
        self.conn.close()


def get_db_conn(db_dir):
    """
    Connect to a sqlite3 database file. Create the database if needed. 
    Not using foreign key constraints to maximize compatibility.
    :param db_dir: The database file to connect to 
    :return: The connection object
    """

    try:
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
    except OSError as e:
            pass

    db_file = os.path.join(db_dir, 'alarms-v%d.db' % SCHEMA_VERSION)
    conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS alarm (
                    volcano text,
                    subject text,
                    message text
                    );''')

    conn.commit()

    return conn
