#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""
<<<<<<< HEAD
=======

>>>>>>> ffae81a3ce80b41a0bf6f1052e6fe1ea544b990d
import MySQLdb
from sys import argv

<<<<<<< HEAD
if __name__ == '__main__':

    db_key = []

    for args in argv[1:]:
        db_key.append(args)

    conn = MySQLdb.connect(
                            host="localhost",
                            port=3306, user=f"{db_key[0]}",
                            passwd=f"{db_key[1]}",
                            db=f"{db_key[2]}"
                          )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

=======

if __name__ == "__main__":      
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],  port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cur.fetchall()
    for line in result:
        print(line)
>>>>>>> ffae81a3ce80b41a0bf6f1052e6fe1ea544b990d
    cur.close()
    conn.close()
