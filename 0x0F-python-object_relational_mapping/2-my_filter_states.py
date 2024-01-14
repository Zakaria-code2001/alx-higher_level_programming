#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    state = state_name_searched  # Assign the state_name_searched directly to state
    query = f"SELECT * FROM states WHERE name LIKE '{state}%' ORDER BY id ASC"
    cursor.execute(query)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

