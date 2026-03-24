from fastapi import APIRouter
from app.services.player_service import get_player_data

router = APIRouter()

@router.get("/player")
def read_player_data():
    return get_player_data()