from fastapi import APIRouter
from app.providers.moviebox.details import get_details

router = APIRouter()


@router.get("/details/{subject_id}")
async def details(subject_id: str):
    return await get_details(subject_id)