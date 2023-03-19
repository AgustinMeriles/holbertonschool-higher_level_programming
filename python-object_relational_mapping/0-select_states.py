#!/usr/bin/python3
"""Shebang"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    mS_username = sys.argv[1]
    mS_password = sys.argv[2]
    d_name = sys.argv[3]

    my_connection = MySQLdb.connect(
        host="localhost",
        user=mS_username,
        passwd=mS_password,
        db=d_name,
        port=3306)
    cur = my_connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for username, password, name in cur.fetchall():
        print(username, password, name)
    my_connection.close()
