import os
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from eralchemy2 import render_er
from datetime import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class UserSW(BaseModel):
    __tablename__ = 'user_sw'
    ID = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    creation = Column(DateTime, default=datetime.utcnow, nullable=False)

    favorites = relationship('Favorites', back_populates='user')

class Planet(BaseModel):
    __tablename__ = 'planet'
    ID = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    diameter = Column(String(50), nullable=False)
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(String(50), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = relationship('Favorites', back_populates='planet')

class People(BaseModel):
    __tablename__ = 'people'
    ID = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    height = Column(String(20), nullable=False)
    mass = Column(String(40), nullable=False)
    skin_color = Column(String(50), nullable=False)
    homeworld = Column(String(100), nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = relationship('Favorites', back_populates='people')

class Vehicle(BaseModel):
    __tablename__ = 'vehicle'
    ID = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    vehicle_class = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    length = Column(String(50), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    max_atmosphering_speed = Column(String(50), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    consumables = Column(String(100), nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = relationship('Favorites', back_populates='vehicle')

class Starship(BaseModel):
    __tablename__ = 'starship'
    ID = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    starship_class = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    passengers = Column(String(50), nullable=False)
    max_atmosphering_speed = Column(String(50), nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    MGLT = Column(String(50), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    consumables = Column(String(100), nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = relationship('Favorites', back_populates='starship')

class Film(BaseModel):
    __tablename__ = 'film'
    ID = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String(1000), nullable=False)
    director = Column(String(100), nullable=False)
    producer = Column(String(200), nullable=False)
    release_date = Column(DateTime, nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = relationship('Favorites', back_populates='film')

class Species(BaseModel):
    __tablename__ = 'species'
    ID = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    classification = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    average_height = Column(String(50), nullable=False)
    average_lifespan = Column(String(50), nullable=False)
    eye_colors = Column(String(100), nullable=False)
    hair_colors = Column(String(100), nullable=False)
    skin_colors = Column(String(100), nullable=False)
    language = Column(String(100), nullable=False)
    homeworld = Column(String(100), nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = relationship('Favorites', back_populates='species')

class Favorites(BaseModel):
    __tablename__ = 'favorites'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_sw.ID'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.ID'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.ID'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.ID'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starship.ID'), nullable=True)
    species_id = Column(Integer, ForeignKey('species.ID'), nullable=True)
    film_id = Column(Integer, ForeignKey('film.ID'), nullable=True)

    user = relationship('UserSW', back_populates='favorites')
    people = relationship('People', back_populates='favorites')
    vehicle = relationship('Vehicle', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    starship = relationship('Starship', back_populates='favorites')
    species = relationship('Species', back_populates='favorites')
    film = relationship('Film', back_populates='favorites')

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

try:
    result = render_er(db.Model, 'diagram.png')
except Exception as e:
    raise e
