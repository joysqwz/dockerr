from fastapi import FastAPI

app = FastAPI()

origins = [
    "http://172.105.0.7:8000",
    "http://172.105.0.8:3000",
    "http://192.168.0.27:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]


@app.get("/")
async def root():
    return {"message": "Hello World"}