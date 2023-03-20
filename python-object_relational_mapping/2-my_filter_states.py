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
    q = ("""SELECT * FROM states WHERE name LIKE {}
    ORDER BY states.id ASC""".format(state_name))
    cur.execute(q)
    for element in cur.fetchall():
        print(element)
