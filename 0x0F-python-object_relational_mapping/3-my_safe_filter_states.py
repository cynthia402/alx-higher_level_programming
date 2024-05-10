#!/usr/bin/python3
""" module that connect ot detabase and fetchall states in safe way'"""


import sys
import MySQLdb


if __name__ == '__main__':
    myDb = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3], port=3306)

    myCursor = myDb.cursor()
    name = sys.argv[4]
    sql = f"SELECT * FROM states WHERE name LIKE BINARY %s\
                       ORDER BY states.id ASC"
    myCursor.execute(sql, (name,))

    all_states = myCursor.fetchall()
    for each in all_states:
        print(each)

    myCursor.close()
    myDb.close()
