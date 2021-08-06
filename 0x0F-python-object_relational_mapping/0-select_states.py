#!/usr/bin/python3
""" Create states table in hbtn_0e_0_usa with some data """

import MySQLdb
import sys
args = sys.argv

db = MySQLdb.connect(localhost=args[1], password=args[2], database=args[3],
                     port=3306)
cursor = db.cursor()
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit the changes
    db.commit()
except:
    # Rollback if there is any error
    db.rollback()
# Disconect from server
db.close()
