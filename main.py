from fastapi import FastAPI
import moviebox_api.v3 as v3

app = FastAPI()

@app.get("/")
async def root():
    return {
        "exports": dir(v3)
    }