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

    cur = myDb.cursor()

    n = sys.argv[4]
    cur.execute("SELECT name from cities WHERE state_id=(SELECT id FROM\
                       states WHERE name=%s) ORDER BY cities.id ASC", (n,))

    all_states = cur.fetchall()
    for idx, each in enumerate(all_states):
        if (idx != 0):
            print(', ', end='')
        print(each[0], end='')

    print()
    cur.close()
    myDb.close()
