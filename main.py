from fastapi import FastAPI
from app.routes.home import router as home_router

app = FastAPI(title="ZenkaiOS Backend")

app.include_router(home_router)


@app.get("/")
async def root():
    return {
        "name": "ZenkaiOS Backend",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {"status": "ok"}