from fastapi import FastAPI

from moviebox_api.v3.http_client import MovieBoxHttpClient
from moviebox_api.v3.core import Homepage

app = FastAPI(title="ZenkaiOS MovieBox Backend")

@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/home")
async def home():
    async with MovieBoxHttpClient() as client:
        homepage = Homepage(client)
        return await homepage.get_content()
