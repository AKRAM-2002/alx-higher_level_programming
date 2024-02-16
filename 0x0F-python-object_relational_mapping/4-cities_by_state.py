#!/usr/bin/python3
import MySQLdb
import sys

def select_cities_by_state(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT c.id, c.name, s.name FROM cities as c JOIN states as s ON c.state_id = s.id ORDER BY c.id" 
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    select_cities_by_state(username, password, database)
