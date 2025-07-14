#!/usr/bin/python3
"""Affiche toutes les villes d'un état donné (sécurisé contre l'injection SQL)."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # Requête paramétrée pour éviter toute injection SQL
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))
    rows = cur.fetchall()
    # On extrait juste les noms des villes
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    cur.close()
    db.close()
