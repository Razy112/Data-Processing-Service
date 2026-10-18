from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "First API path"}

@app.get("/health")
async def root():
    return {"message": "JSON"}
    