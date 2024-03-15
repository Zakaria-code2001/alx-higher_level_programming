#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves data from a table called 'states'.
"""

import MySQLdb
import sys


def retrieve_states(username, password, db_name):
    """
    Retrieve states data from a MySQL database.

    Args:
        username (str): The username for the database connection.
        password (str): The password for the database connection.
        db_name (str): The name of the database to connect to.

    Returns:
        list: A list of tuples representing the retrieved data.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        results = cursor.fetchall()

        return results

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    states_data = retrieve_states(username, password, db_name)

    for row in states_data:
        print(row)
