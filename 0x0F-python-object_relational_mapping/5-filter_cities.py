#!/usr/bin/python3
""" Create states table in hbtn_0e_0_usa with some data """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting with database
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8")
    # Creating the cursor
    cur = db.cursor()
    # Executing the Query
    name = argv[4]
    cur.execute(
        "SELECT cities.name\
            FROM states INNER JOIN cities ON states.id = cities.state_id\
            WHERE states.name = %s", (name,))
    # Selecting the information
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    # Closing cursor
    cur.close()
    # Closing database
    db.close()
