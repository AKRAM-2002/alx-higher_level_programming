#!/usr/bin/python3
import MySQLdb
import sys

def filter_cities(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = """
        SELECT c.name 
        FROM cities as c 
        JOIN states as s 
        ON c.state_id = s.id
        WHERE s.name = %s 
        ORDER BY c.id ASC
    """ 
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    cities = [row[0] for row in results]

    print(', '.join(cities))

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    filter_cities(username, password, database, state_name)
