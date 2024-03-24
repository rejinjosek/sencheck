from fastapi import FastAPI
from router import router

app = FastAPI(version='1.0')


app.include_router(router, prefix="/api/v1")

@app.get("/version")
def check_version():
    return app.version


#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="0.0.0.0", port=8000)