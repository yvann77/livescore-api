from pydantic import BaseModel
from typing import List

class League(BaseModel):
    name: str
    country: str

# No IDs for POST requests   
class LeagueNoID(BaseModel):
    name: str
    country: str

class Match(BaseModel):
    id : str
    equipe_domicile: str
    equipe_exterieure: str
    score_domicile: int
    score_exterieur: int
    competition: str
    statut : str
    minute: int

class MatchNoID(BaseModel):
    equipe_domicile: str
    equipe_exterieure: str
    score_domicile: int
    score_exterieur: int
    competition: str
    statut : str
    minute: int

class User(BaseModel):
    email:str
    password: str

class Standing(BaseModel):
    id: str
    name: str
    competition: str
    wins: int
    losses: int
    draws: int
    points: int
    place : str

class StandingNoID(BaseModel):
    name: str
    competition: str
    wins: int
    losses: int
    draws: int
    points: int
    place : str



class StandingNoName(BaseModel):
    competition: str
    wins: int
    losses: int
    draws: int
    points: int
    place : str