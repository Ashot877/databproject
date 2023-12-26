from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    results = relationship('Result', back_populates='team')

class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime)
    venue = Column(String)
    results = relationship('Result', back_populates='game')

class Result(Base):
    __tablename__ = 'results'
    
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    score = Column(Integer)  
    
    team = relationship('Team', back_populates='results')
    game = relationship('Game', back_populates='results')

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.create_all(engine)
