#!/usr/bin/python3
"""
Wait, do you remember the previous task? Did you test
"Arizona'; TRUNCATE TABLE states ;
SELECT * FROM states WHERE name = '" as an input?
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name = %s ORDER BY id ASC")
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
