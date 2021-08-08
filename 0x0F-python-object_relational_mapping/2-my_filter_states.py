#!/usr/bin/python3
""" Create states table in hbtn_0e_0_usa with some data """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting with database
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3],
                         port=3306, charset="utf8")
    # Creating the cursor
    cur = db.cursor()
    # Executing the Query
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4]))
    # Selecting the information
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    # Closing cursor
    cur.close()
    # Closing database
    db.close()
