#!/usr/bin/python3
"""Affiche toutes les valeurs de la table states correspondant à un nom donné, de façon sécurisée."""

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
    # Requête paramétrée pour éviter toute injection SQL
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
