#!/usr/bin/python3
"""
    A script that takes in an argument and displays 
    all values in the states table of hbtn_0e_0_usa 
    where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    except Exception:
        print('Failed to connect to the database')
        exit(0)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '" + state + "' ORDER BY id ASC;" 
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
