from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
from classes.schema_dto import League, LeagueNoID
router = APIRouter(
    tags=['Leagues']
)


leagues = [
    League(name="Premier League", matchs = [
    {"équipe_domicile": "Aston Villa", "équipe_visiteuse": "Tottenham"},{"équipe_domicile": "Arsenal", "équipe_visiteuse": "Manchester City"},]),
    League(name="Ligue 1", matchs=[{"équipe_domicile": "Lorient","équipe_visiteuse": "Rennes",},{"équipe_domicile": "Toulouse","équipe_visiteuse": "Reims"},]),
    League(name="Liga", matchs=[{ "équipe_domicile": "Villarreal","équipe_visiteuse": "UD Las Palmas",},{"équipe_domicile": "Atlético Madrid","équipe_visiteuse": "Real Sociedad",},])
]

@router.get("/leagues", tags=["Leagues"])
async def get_leagues():
    return leagues


@router.post('/leagues', tags=["Leagues"])
async def create_league(givenLeague:LeagueNoID):
    newLeague= League(givenLeague)
    leagues.append(newLeague)
    return newLeague


@router.patch('/leagues/{name}')
async def modify_league(name:str, modifiedLeague:LeagueNoID):
    for league in leagues : 
        if league.name == name and league.matchs == modifiedLeague.matchs:
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