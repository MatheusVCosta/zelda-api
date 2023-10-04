from fastapi import APIRouter

from app.config.config import get_settings
from app.services.zelda_api_connector import ZeldaAPIConnector
import json
import requests
router = APIRouter(
    prefix="/games",
    tags=["games"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("")
def index():
    connector = ZeldaAPIConnector()
    games = connector.fetch_all_games()
    url = f"{get_settings().firebase_uri}/games/.json"
    
    for game in games['data']:
        response = requests.post(url, data=json.dumps(game))
        if response.status_code == 404:
            print("Some error")
        
    return response