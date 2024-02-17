#!/usr/bin/python3
"""
Lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    query = "SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' ORDER BY id ASC;" 
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

