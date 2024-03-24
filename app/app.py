import logging
from fastapi import FastAPI
from router import router

logging.basicConfig(level=logging.INFO)
app = FastAPI(version='1.0', title='Sencheck: A sentiment analyzer API')

app.include_router(router, prefix="/api/v1")

@app.get("/version")
def check_version():
    return app.version
