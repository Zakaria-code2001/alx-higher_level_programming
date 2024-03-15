#!/usr/bin/python3
"""
Script to query states starting with 'N' from a MySQL database.
"""

import MySQLdb
import sys


def query_states(username, password, db_name, state_name):
    """
    Query states from the specified MySQL database.

    Args:
        username (str): Username to connect to the MySQL database.
        password (str): Password to connect to the MySQL database.
        db_name (str): Name of the MySQL database.
        state_name (str): Name of the state to query.

    Returns:
        list: A list of tuples representing the query results.
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()

    query = ("SELECT * FROM states WHERE name = %s ORDER BY id ASC LIMIT 1")
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: <username> <password> <db_name> <state_name>")

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    states = query_states(username, password, db_name, state_name)
    for state in states:
        print(state)
