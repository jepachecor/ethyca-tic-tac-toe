from fastapi import FastAPI
from app.api.routers.players import router as player_router

app = FastAPI()

app.include_router(player_router)