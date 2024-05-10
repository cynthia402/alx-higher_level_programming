#!/usr/bin/python3
""" module that connect ot detabase and fetchall states start with 'N'"""


import sys
import MySQLdb


if __name__ == '__main__':
    myDb = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3], port=3306)

    myCursor = myDb.cursor()

    myCursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                      ORDER BY states.id ASC".format(sys.argv[4]))

    all_states = myCursor.fetchall()
    for each in all_states:
        print(each)

    myCursor.close()
    myDb.close()
