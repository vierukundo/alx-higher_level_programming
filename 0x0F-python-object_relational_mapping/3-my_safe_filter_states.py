#!/usr/bin/python3
"""a Python library that provides an interface
for interacting with MySQL databases"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE states.name \
            LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (state,))
    states_rows = cur.fetchall()
    for state in states_rows:
        print(state)
    cur.close()
    conn.close()
