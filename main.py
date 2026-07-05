from fastapi import FastAPI
from moviebox_api.v3.http_client import MovieBoxHttpClient
from moviebox_api.v3.core import Homepage, ItemDetails

app = FastAPI(title="ZenkaiOS MovieBox Backend")


@app.get("/")
async def root():
    return {
        "status": "ok",
        "provider": "moviebox",
        "version": "v3"
    }


@app.get("/home")
async def home():
    async with MovieBoxHttpClient() as client:
        homepage = Homepage(client)
        return await homepage.get_content()

@app.get("/details/{subject_id}")
async def details(subject_id: str):
    async with MovieBoxHttpClient() as client:
        details = ItemDetails(client)
        return await details.get_content(subject_id)