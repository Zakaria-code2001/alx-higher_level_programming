#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name_searched)
    cursor.execute(query)

    # Fetch all the rows using fetchall() method
    data = cursor.fetchall()

    # Display results
    for row in data:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

