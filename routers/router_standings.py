from fastapi import APIRouter, Depends, HTTPException
import uuid
from classes.schema_dto import Standing, StandingNoID
from database.firebase import db
from routers.router_auth import get_current_user

router = APIRouter(
    tags=['Standings']
)


@router.get('/standing/{team_id}', response_model=Standing)
async def get_standing_by_teamid(team_id: uuid.UUID, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child('standings').child(userData['uid']).child('standing').child(str(team_id)).get(userData['idToken']).val()
    if fireBaseobject is not None:
        return fireBaseobject
    raise HTTPException(status_code= 404, detail="Team Standing not found")


# @router.post('/standing', response_model=Standing, status_code=201)
# async def create_standing(givenStanding: StandingNoID, userData: int = Depends(get_current_user)):
    # generatedId=uuid.uuid4()
    # newStanding= Standing(id=str(generatedId), name = givenStanding.name, competition = givenStanding.competition, wins = givenStanding.wins, losses = givenStanding.losses, draws = givenStanding.draws, points= givenStanding.points, place = givenStanding.place)
    # db.child('standings').child(userData['uid']).child("standing").child(str(generatedId)).set(newStanding.dict(), token=userData['idToken'])
    # return newStanding


@router.patch('/standings/{team_id}', status_code=204)
async def modify_team_standing(team_id:str, modifiedStanding: StandingNoID, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child('matchs').child(userData['uid']).child('match').get(userData['idToken']).val()
    if fireBaseobject is not None:
        updatedStanding = Standing(id=str(team_id), **modifiedStanding.dict())
        return db.child('standings').child(userData['uid']).child('standing').child().update(updatedStanding.dict(), userData['idToken'])
    raise HTTPException(status_code= 404, detail="Standing not found")