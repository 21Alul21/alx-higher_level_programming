#!/bin/usr/python3

"""
this sccript lists all states from the database hbtn_0e_0_usa,     
the script takes 3 arguments: mysql username, mysql password
and database name
"""


import MySQLdb
import sys

if __name__ == "__main__":

        username = sys.arg[1]
        password = sys.arg[2]
        database = sys.arg[3]        
        conn = MySQLdb.connect(user=username, passwd=password,
                               db=database, host="localhost", port=3306)
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        result = cur.fetchall()
        
        for line in result:
            print(result)
            cur.close()
            conn.close()

