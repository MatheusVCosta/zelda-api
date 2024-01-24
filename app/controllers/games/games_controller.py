from fastapi import APIRouter

from app.config.config import get_settings
from app.services.zelda_api_connector import ZeldaAPIConnector

router = APIRouter(
    prefix="/games",
    tags=["games"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("")
def getAllGames(limit: int = 1):
    params = {
        "limit" : limit
    }
    connector = ZeldaAPIConnector()
    response = connector.fetch_all_games(params)
    return response

    # url = f"{get_settings().firebase_uri}games/.json"
    # for game in games['data']:
    #     data=json.dumps(game)
    #     response = requests.get(url, data)
        
    #     response = requests.post(url, data)
    #     if response.status_code >= 400:
    #         print("Some error")
        
    