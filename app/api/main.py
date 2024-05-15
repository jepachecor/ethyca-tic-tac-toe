from fastapi import FastAPI
from app.api.routers.player_router import router as player_router
from app.api.routers.game_router import router as game_router
from app.api.routers.move_router import router as move_router

app = FastAPI()

app.include_router(player_router)
app.include_router(game_router)
app.include_router(move_router)