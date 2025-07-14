#!/usr/bin/python3
"""Définition de la classe State pour SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création de la base de classes pour SQLAlchemy
Base = declarative_base()

class State(Base):
    """Classe State liée à la table 'states' de MySQL."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
