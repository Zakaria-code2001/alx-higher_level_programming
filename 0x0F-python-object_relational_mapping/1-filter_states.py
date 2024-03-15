#!/usr/bin/python3
"""
Script to query states startin with 'N' from a MySQL database.
"""

import MySQLdb
import sys


def query_states(username, password, db_name):
    """
    Query states from the specified MySQL database.

    Args:
        username (str): The username to connect to the MySQL database.
        password (str): The password to connect to the MySQL database.
        db_name (str): The name of the MySQL database.

    Returns:
        list: A list of tuples representing the query.
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC LIMIT 2"
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    states = query_states(username, password, db_name)
    for state in states:
        print(state)
