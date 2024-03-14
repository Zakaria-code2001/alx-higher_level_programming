#!/usr/bin/python3
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
    query = ("SELECT cities.name "
             "FROM cities JOIN states "
             "ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC LIMIT 3")
    cursor.execute(query, (state_name,))

    city_names = []
    for row in cursor.fetchall():
        city_names.append(row[0])

    print(', '.join(city_names))

    cursor.close()
    db.close()
