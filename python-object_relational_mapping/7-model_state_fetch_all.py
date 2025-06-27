#!/usr/bin/python3
"""Liste tous les objets State de la base hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Création de l'engine de connexion à la base MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération et affichage des objets State triés par id croissant
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()
