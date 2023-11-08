from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid
from classes.schema_dto import Match, MatchNoID
from database.firebase import db
from routers.router_auth import get_current_user

router = APIRouter(
    tags=['Matches']
)



@router.get('/matchs', response_model=List[Match])
async def get_matches(userData: int = Depends(get_current_user)):
    fireBaseobject = db.child('matchs').child(userData['uid']).child('match').get(userData['idToken']).val()
    resultArray = [value for value in fireBaseobject.values()]
    return resultArray


from fastapi import Depends, Query
from typing import List

@router.get('/matchs/{team_id}/competition', response_model=List[Match])
async def get_matches_per_competition(userData: int = Depends(get_current_user), competition: str = Query(None)):
    fireBaseobject = db.child('matchs').child(userData['uid']).child('match').get(userData['idToken']).val()
    if competition:
        resultArray = [value for value in fireBaseobject.values() if value.get('competition') == competition]
        return resultArray
    raise HTTPException(status_code= 404, detail="Competition not found")



@router.post('/matchs', response_model=Match, status_code=201)
async def create_match(givenMatch: MatchNoID, userData: int = Depends(get_current_user)):
    generatedId=uuid.uuid4()
    newMatch= Match(id=str(generatedId), equipe_domicile = givenMatch.equipe_domicile, equipe_exterieure = givenMatch.equipe_exterieure, score_domicile = givenMatch.score_domicile, score_exterieur = givenMatch.score_exterieur,competition= givenMatch.competition, statut = givenMatch.statut, minute= givenMatch.minute)
    db.child('matchs').child(userData['uid']).child("match").child(str(generatedId)).set(newMatch.dict(), token=userData['idToken'])
    return newMatch


@router.patch('/{match_id}', status_code=204)
async def modify_match(match_id:str, modifiedMatch: MatchNoID, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child('matchs').child(userData['uid']).child('match').get(userData['idToken']).val()
    if fireBaseobject is not None:
        updatedMatch = Match(id=str(match_id), **modifiedMatch.dict())
        return db.child('matchs').child(userData['uid']).child('match').child(match_id).update(updatedMatch.dict(), userData['idToken'])
    raise HTTPException(status_code= 404, detail="Match not found")


# @router.delete('/{match_id}', status_code=204)
# async def delete_match(match_id:str, userData: int = Depends(get_current_user)):
   # try:
     #   fireBaseobject = db.child('matchs').child(userData['uid']).child('match').get(userData['idToken']).val()
   # except:
       # raise HTTPException(
       #     status_code=403, detail="Accès interdit"
      #  )
    # if fireBaseobject is not None:
     #   return db.child("matchs").child(userData['uid']).child('match').child(match_id).remove(userData['idToken'])
    # raise HTTPException(status_code= 404, detail="Session not found")