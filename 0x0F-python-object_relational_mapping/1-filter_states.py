#!/usr/bin/python3

"""
python script that lists all states with a name starting with N(upper N) from
the database hbtn_0e_0_usa
the script takes three arguments
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(user=username, passwd=password, db=database, host=localhost, port=3306)
    cur = conn.cursor()
    cur.execute("SELECT name, id FROM states WHERE name LIKE "N%" ORDER BY id ASC")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()


