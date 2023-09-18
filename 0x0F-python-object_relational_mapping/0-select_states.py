#!/usr/bin/python3
"""
this sccript lists all states from the database hbtn_0e_0_usa,     
the script takes 3 arguments: mysql username, mysql password
and database name
"""

import MySQLdb
import sys


if __name__ == "__main__":      
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],  port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cur.fetchall()
    for line in result:
        print(line)
    cur.close()
    conn.close()
