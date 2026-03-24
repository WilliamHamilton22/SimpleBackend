from fastapi import APIRouter
from app.services.crowd_service import get_crowd_data

router = APIRouter()

@router.get("/crowd")
def read_crowd_data():
    return get_crowd_data()