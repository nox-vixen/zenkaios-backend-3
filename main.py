from fastapi import FastAPI
from moviebox_api.v3 import MovieBoxHttpClient, Homepage

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