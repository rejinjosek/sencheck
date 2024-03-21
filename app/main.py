from fastapi import FastAPI
from router import router

app = FastAPI()


app.include_router(router, prefix="/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)