
# Create a Postgres database with tables and perform crud operations.
# save babynames(extracted previously with regex) to postgres table.

from dotenv import load_dotenv
import os
from psycopg2 import connect
import re

load_dotenv('.env')

DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')

"""
performing CURD operation on the baby names in postgres
"""

list_of_name = []

with open('baby2008.html', 'r') as f:
    line = ''
    while True:
        line = f.readline()
        patten = re.compile(r'(><td>)+([a-zA-Z]+)+(</td><)+', re.IGNORECASE)
        matches = re.finditer(pattern=patten, string=line)
        for match in matches:
            gp = match.group(2)
            list_of_name.append(gp)
        if not line:
            break

list_of_name.sort()


class BabyNames:
    conn = None
    def __init__(self):
        try:
            print(DATABASE)
            self.conn = connect(
                dbname=DATABASE,
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT
            )
            print("Connection successful")
        except Exception as e:
            print(f"Error: {e}")

    def addBabyNames(self, list_of_BabyNames):
        if len(list_of_BabyNames)>0:
            for name in list_of_BabyNames:
                cur = self.conn.cursor()
                cur.execute(
                    f"""
                        INSERT INTO BabyNames(names)
                        VALUES('{name}');
                    """
                )
                self.conn.commit()
                cur.close()

    def getBabyNames(self):
        cur = self.conn.cursor()
        cur.execute(
            """
                SELECT id,names FROM BabyNames
            """
        )
        rows = cur.fetchall()
        self.conn.commit()
        cur.close()
        for row in rows:
            print(f'ID:{row[0]} Name:{row[1]}')

    def updateBabyName(self, id,NewTask):
        cur = self.conn.cursor()
        cur.execute(
            f"""
                UPDATE BabyNames
                SET task = {NewTask}
                WHERE id = {id}
            """
        )
        self.conn.commit()
        cur.close()

    def deleteBabyName(self, id):
        cur = self.conn.cursor()
        cur.execute(
            f"""
                DELETE FROM BabyNames
                WHERE id = {id};
             """
        )
        self.conn.commit()
        cur.close()


BabyNames = BabyNames()
BabyNames.addBabyNames(list_of_name)
BabyNames.getBabyNames()
# BabyNames.deleteBabyName(id=1)
# BabyNames.updateBabyName(id=2)
