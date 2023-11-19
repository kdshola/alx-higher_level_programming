#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa here name matches
the argument.. Takes 4 arguments: mysql username, mysql password and database
name and state name searched
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
            WHERE name = "{}"
            ORDER BY states.id""".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
