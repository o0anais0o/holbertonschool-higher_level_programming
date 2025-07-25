#!/usr/bin/python3
"""Ce script liste tous les états de la table states de la base hbtn_0e_0_usa.
Il prend 3 arguments : nom d'utilisateur MySQL, mot de passe MySQL, nom de la base de données.
Les résultats sont triés par id croissant.
"""

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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
