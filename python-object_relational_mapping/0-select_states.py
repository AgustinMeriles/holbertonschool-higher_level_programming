#!/usr/bin/python3
"""Shebang"""

if __name__ == '__main__':
    import MySQLdb

    my_connection = MySQLdb.connect(host="localhost",  port=3306)
    cur = my_connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for username, password, name in cur.fetchall():
        print(username, password, name)
    my_connection.close()
