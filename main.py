from fastapi import FastAPI
import pkgutil
import moviebox_api.v3

app = FastAPI()

@app.get("/")
async def root():
    return {
        "modules": [
            m.name for m in pkgutil.iter_modules(moviebox_api.v3.__path__)
        ]
    }