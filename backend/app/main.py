from fastapi import FastAPI
from app.routes.player_routes import router as player_router
from app.routes.crowd_routes import router as crowd_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

app.include_router(player_router, prefix="/api", tags=["Player"])
app.include_router(crowd_router, prefix="/api", tags=["Crowd"])