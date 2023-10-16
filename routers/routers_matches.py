from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from pydantic import BaseModel
import uuid
from classes.schema_dto import Match, MatchNoID

router = APIRouter(
    tags=['Matches']
)

matches = [
    Match(
        id="1",
        équipe_domicile="Paris Saint-Germain",
        équipe_extérieure="AS Monaco",
        score_domicile=2,
        score_extérieure=1,
        statut="Terminé",
        minute=90,
    ),
    Match(
        id="2",
        équipe_domicile="Olympique de Marseille",
        équipe_extérieure="Olympique Lyonnais",
        score_domicile=3,
        score_extérieure=2,
        statut="Terminé",
        minute=90,
    ),
    Match(
        id="3",
        équipe_domicile="FC Barcelone",
        équipe_extérieure="Real Madrid",
        score_domicile=1,
        score_extérieure=0,
        statut="Terminé",
        minute=90,
    ),
]
@router.get('/', response_model=List[Match])
async def get_matches():
    return matches

@router.post('/', response_model=Match, status_code=201)
async def create_match(givenMatch: MatchNoID):
    generatedId=uuid.uuid4()
    newMatch= Match(id=str(generatedId), **givenMatch)
    matches.append(newMatch)
    return newMatch

@router.get('/{match_id}', response_model=Match)
async def get_match_by_ID(match_id:str): 
    for match in matches:
        if match.id == match_id:
            return match
    raise HTTPException(status_code= 404, detail="Match not found")

@router.patch('/{match_id}', status_code=204)
async def modify_match(match_id:str, modifiedMatch: MatchNoID):
    for match in matches:
        if match.id == match_id:
            match.équipe_domicile = modifiedMatch.équipe_domicile
            match.équipe_extérieure = modifiedMatch.équipe_extérieure
            return
    raise HTTPException(status_code= 404, detail="Match not found")

@router.delete('/{match_id}', status_code=204)
async def delete_match(match_id:str):
    for match in matches:
        if match.id == match_id:
            matches.remove(match)
            return
    raise HTTPException(status_code= 404, detail="Match not found")