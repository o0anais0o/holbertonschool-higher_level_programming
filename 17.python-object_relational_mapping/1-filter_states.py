#!/usr/bin/python3
"""Répertorie tous les états dont le nom commence par « N » de la base de données hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
