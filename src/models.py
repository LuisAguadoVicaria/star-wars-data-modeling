import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
favorites_table = Table(
    "favorites",
    Base.metadata,
    Column("usuarios_id", ForeignKey("usuarios.id")),
    Column("planetas_id", ForeignKey("planetas.id")),
    Column("personajes_id", ForeignKey("personajes.id")),
)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(DateTime(False), nullable=False)
    planets_ids = relationship("Planets", secondary=favorites_table)
    characters_ids = relationship("Characters", secondary=favorites_table)

class Planets(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    latitude_longitude = Column(String(250))

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    bio = Column(String(250))
    birth_planet = relationship("Planets", back_populates="personajes")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')