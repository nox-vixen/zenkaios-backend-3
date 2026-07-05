from fastapi import FastAPI

app = FastAPI(
    title="ZenkaiOS Backend",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "name": "ZenkaiOS Backend",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }