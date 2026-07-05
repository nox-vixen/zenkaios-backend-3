from fastapi import FastAPI
import pkgutil
import moviebox_api.v3

from app.routes.home import router as home_router

app = FastAPI()

app.include_router(home_router)

@app.get("/")
async def root():
    return {
        "modules": [
            m.name for m in pkgutil.iter_modules(moviebox_api.v3.__path__)
        ]
    }

@app.get("/health")
async def health():
    return {"status": "ok"}
