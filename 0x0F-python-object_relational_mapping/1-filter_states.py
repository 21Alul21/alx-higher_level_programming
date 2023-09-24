#!/usr/bin/python3
<<<<<<< HEAD
=======

>>>>>>> ffae81a3ce80b41a0bf6f1052e6fe1ea544b990d
"""
List all states with name starting with N.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db_key = []

    for args in argv[1:]:
        db_key.append(args)

    db = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=f"{db_key[0]}",
      passwd=f"{db_key[1]}",
      db=f"{db_key[2]}"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE states.name LIKE BINARY 'N%' ORDER BY states.id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

<<<<<<< HEAD
=======
    conn = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY 'N%' ORDER BY states.id ASC")
    result = cur.fetchall()
    for row in result:
        print(row)
>>>>>>> ffae81a3ce80b41a0bf6f1052e6fe1ea544b990d
    cur.close()
    db.close()
