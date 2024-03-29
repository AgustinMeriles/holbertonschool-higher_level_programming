#!/usr/bin/python3
"""Shebang"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    mS_username = sys.argv[1]
    mS_password = sys.argv[2]
    d_name = sys.argv[3]
    state_name = sys.argv[4]

    my_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mS_username,
        passwd=mS_password,
        db=d_name)

    cur = my_connection.cursor()
    q = ("""SELECT cities.name FROM cities JOIN states ON
    cities.state_id = states.id WHERE states.name LIKE BINARY '{}'
    ORDER BY cities.id ASC""".format(state_name,))
    cur.execute(q)

    for i, city in enumerate(cur.fetchall()):
        if i != 0:
            print(", ", end="")
        print(city[0], end="")
    print()
