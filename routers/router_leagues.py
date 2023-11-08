from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
from classes.schema_dto import League, LeagueNoID
router = APIRouter(
    tags=['Leagues']
)


leagues = [
    League(name="Champions League", country = "UEFA"),
    League(name="Premier League", country = "Angleterre"),
    League(name="Ligue 1", country = "France"),
    League(name="Liga",country = "Espagne"),
    League(name="Bundesliga", country = "Allemagne")
]

@router.get("/leagues", tags=["Leagues"])
async def get_leagues():
    return leagues


@router.post('/leagues', tags=["Leagues"])
async def create_league(givenLeague:LeagueNoID):
    newLeague = League(name = givenLeague.name, country= givenLeague.country)
    leagues.append(newLeague)
    return newLeague


@router.patch('/leagues/{name}')
async def modify_league(name:str, modifiedLeague:LeagueNoID):
    for league in leagues : 
        if league.name == name and league.country == modifiedLeague.country:
            league.name = modifiedLeague.name      
            return league
    raise HTTPException(status_code= 404, detail="League not found")

@router.delete('/leagues/{name}', status_code=204)
async def delete_league(name:str):
    for league in leagues : 
        if league.name == name:
            leagues.remove(league)
            return
    raise HTTPException(status_code= 404, detail="League not found")