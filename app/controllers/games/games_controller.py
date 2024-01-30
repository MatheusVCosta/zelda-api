from fastapi import Depends, FastAPI, HTTPException, APIRouter
from app.config.config import get_settings
from app.services.zelda_api_connector import ZeldaAPIConnector
from app.models import Game
from sqlalchemy.orm import Session

from app.database import SessionLocal

router = APIRouter(
    prefix="/games",
    tags=["games"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("")
def getAllGames(db: Session = Depends(get_db)):
    # params = {
    #     "limit" : limit
    # }
    # connector = ZeldaAPIConnector()
    # response = connector.fetch_all_games(params)
    game = Game()
    return game.get_game(db, 'Zelda')

    # url = f"{get_settings().firebase_uri}games/.json"
    # for game in games['data']:
    #     data=json.dumps(game)
    #     response = requests.get(url, data)
        
    #     response = requests.post(url, data)
    #     if response.status_code >= 400:
    #         print("Some error")
        
    