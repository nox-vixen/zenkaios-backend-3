from fastapi import APIRouter
from app.providers.moviebox.home import get_home

router = APIRouter()

@router.get("/home")
async def home():
    return await get_home()