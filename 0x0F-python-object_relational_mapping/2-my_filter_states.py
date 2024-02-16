#!/usr/bin/python3
import MySQLdb
import sys

def filter_states(username, password, database, state):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '" + state + "' ORDER BY id ASC" 
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    filter_states(username, password, database, state)
