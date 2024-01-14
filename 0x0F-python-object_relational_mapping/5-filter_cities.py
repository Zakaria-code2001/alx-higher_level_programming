#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state
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

    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name_searched,))

    data = cursor.fetchall()

    # Extract city names from the result set
    cities = []
    for row in data:
        cities.append(row[0])
    # Print the results as a comma-separated string
    print(', '.join(cities))

    cursor.close()
    db.close()

