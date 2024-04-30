#!/usr/bin/python3
""" module that connect ot detabase and fetchall cities'"""


import sys
import MySQLdb


if __name__ == '__main__':
    myDb = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3], port=3306)

    myCursor = myDb.cursor()

    sql = f"SELECT id, name, (SELECT name FROM states\
    WHERE id=cities.state_id) FROM cities ORDER BY cities.id ASC"
    myCursor.execute(sql)

    all_states = myCursor.fetchall()
    for each in all_states:
        print(each)

    myCursor.close()
    myDb.close()
