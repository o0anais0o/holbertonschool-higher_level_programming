#!/usr/bin/python3
"""Répertorie toutes les valeurs dans la table des états où le nom correspond à l'argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # Attention: format() utilisé comme demandé (risque d'injection SQL !)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
