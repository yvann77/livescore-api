from pydantic import BaseModel
from typing import List

class League(BaseModel):
    name: str
    matchs: List[dict]  

# No IDs for POST requests   
class LeagueNoID(BaseModel):
    name:str
    matchs: List[dict] 

class Match(BaseModel):
    équipe_domicile: str
    équipe_extérieure: str
    score_domicile: int
    score_extérieur: int
    statut: str
    minute: int

class MatchNoID(BaseModel):
    équipe_domicile: str
    équipe_extérieure: str

class Match(MatchNoID):
    id: str
    