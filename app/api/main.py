from fastapi import FastAPI
from app.api.routers.player_router import router as player_router
from app.api.routers.game_router import router as game_router

app = FastAPI()

app.include_router(player_router)
app.include_router(game_router)