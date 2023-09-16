#!/usr/bin/python3
"""a Python library that provides an interface
for interacting with MySQL databases"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities JOIN states \
    ON cities.state_id = states.id \
    WHERE states.name = %s \
    ORDER BY cities.id ASC"
    cur.execute(query, (sys.argv[4], ))
    cities = cur.fetchall()
    if cities:
        city_names = [city[0] for city in cities]
    print(", ".join(city_names))
    cur.close()
    conn.close()
