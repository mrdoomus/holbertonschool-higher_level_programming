#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
    FROM cities INNER JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4],))
    cities = ''
    for data in cur.fetchall():
        cities += data[0] + ', '
    print(cities[:-2])
