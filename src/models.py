import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_de_suscripción = Column(Date)
    favorite = relationship("Favorite", uselist=False, back_populates="usuario")
    
class Favorite(Base):
    __tablename__ = 'favorite'
 
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario",back_populates="favorite")

    def to_dict(self):
        return {}

class Films(Base):
    __tablename__ = 'films'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    opening_crawl = Column(String(250), nullable=False) 
    director = Column(String(250), nullable=False)
    producer = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship("Favorite")

    def to_dict(self):
        return {}
    
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Date)
    species = Column(String(250), nullable=False) 
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_Color = Column(String(250), nullable=False)
    skin_Color = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship("favorite")
    films_id = Column(Integer, ForeignKey('films.id'))
    film = relationship("films")

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
 
    id = Column(Integer, primary_key=True)
    population = Column(Integer, nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    gravity =Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water =Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship("Usuario")
    films_id = Column(Integer, ForeignKey('films.id'))
    film = relationship("films")

    def to_dict(self):
        return {}
    
class Starships(Base):
    __tablename__ = 'starships'
    
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew =Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity =Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    MGLT = Column(Integer, nullable=False)
    Starships = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship("Favorite")
    films_id = Column(Integer, ForeignKey('films.id'))
    film = relationship("films")

    def to_dict(self):
        return {}
    

# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e