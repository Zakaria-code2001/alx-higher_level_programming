#!/usr/bin/python3
"""
Script to retrieve and display all states from the 'states' table in a MySQL database
"""
import MySQLdb
import sys

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC;"
    cursor.execute(query)
    results = cursor.fetchall()

    for x in results:
        print(x)
      
    cursor.close()
    db.close()

