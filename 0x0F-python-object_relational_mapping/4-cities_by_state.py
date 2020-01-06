#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities, states\
    WHERE cities.state_id = states.id\
    ORDER BY cities.id ASC")
    res = cur.fetchall()
    for data in res:
        print(data)