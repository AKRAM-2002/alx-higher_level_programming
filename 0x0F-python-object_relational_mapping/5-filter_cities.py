#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state, using
the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    import re
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]


    if (re.search('^[a-zA-Z ]+$', state_name) is None):
        print('Enter a valid name state (example: Nevada)')
        exit(1)

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    except Exception:
        print('Failed to connect to the database')
        exit(0)
    cursor = db.cursor()

    query = """
        SELECT c.name 
        FROM cities as c 
        JOIN states as s 
        ON c.state_id = s.id
        WHERE s.name = '{:s}'
        ORDER BY c.id ASC;
    """.format(state_name) 
    cursor.execute(query)
    results = cursor.fetchall()

    cities = [row[0] for row in results]

    print(', '.join(cities))

    cursor.close()
    db.close()
