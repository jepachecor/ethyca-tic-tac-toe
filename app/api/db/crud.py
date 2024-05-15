from sqlalchemy.orm import Session
from app.api.models import *
from app.api.schemas import *
from sqlalchemy import desc
import random

def get_user_by_username(db: Session, username: str):
    return db.query(player_model.Player).filter(player_model.Player.username == username).first()

def get_user_by_id(db: Session, id: int):
    return db.query(player_model.Player).filter(player_model.Player.id == id).first()

def create_player(db: Session, player: player_schema.PlayerIn):
    db_user = player_model.Player(
        username = player.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_game(db: Session, game: game_schema.GameIn):
    db_game = game_model.Game(
        player_id = game.player_id
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def list_games_by_player(db: Session, player_id: int):
    player = get_user_by_id(db=db, id=player_id)
    if player:
        return db.query(game_model.Game).filter_by(player_id=player_id).order_by(desc(game_model.Game.timestamp)).all()
    return None

def create_move(db: Session, move: move_schema.MoveIn):

    if move.x < 0 or move.x > 2 or move.y < 0 or move.y > 2:
            return {
                "detail" : "Not a valid move!"
            }
    
    for game_move in get_moves_by_game(db, move.game_id):
        if game_move.x == move.x and game_move.y == move.y:
            return {
                "detail" : "Not a valid move!"
            }

    save_move(db=db, move=move, player_id=move.player_id)
    board = get_board(db, move.game_id, move.player_id)
    if check_winner(board, symbol='X'):
        user = get_user_by_id(db, move.player_id)
        cpu = get_user_by_id(db, 1)
        user.wins += 1
        cpu.losses += 1
        db.commit()
        return {
                "detail" : "YOU WIN!",
                "board" : board
            }
    
    available_moves = [(i, j) for i in range(3) for j in range(3) if (i, j) not in [(move.x, move.y) for move in get_moves_by_game(db, move.game_id)]]
    if not available_moves:
        user = get_user_by_id(db, move.player_id)
        cpu = get_user_by_id(db, 1)
        user.draws += 1
        cpu.draws += 1
        db.commit()
        return {
                "detail" : "DRAW!",
                "board" : board
            }
    
    cpu_x, cpu_y = random.choice(available_moves)
    move.x, move.y = cpu_x, cpu_y
    save_move(db=db, move=move, player_id=1)
    board = get_board(db, move.game_id, move.player_id)
    if check_winner(board, symbol='O'):
        user = get_user_by_id(db, move.player_id)
        cpu = get_user_by_id(db, 1)
        user.losses += 1
        cpu.wins += 1
        db.commit()
        return {
                "detail" : "YOU LOSE!",
                "board" : board
            }
    
    return {
        "detail" : "Your turn!", 
        "board" : board
    }

def get_moves_by_game(db: Session, game_id: int):
    return db.query(move_model.Move).filter(move_model.Move.game_id == game_id).order_by(desc(move_model.Move.timestamp)).all()

def save_move(db: Session, move: move_schema.MoveIn, player_id: int):
    db_user_move = move_model.Move (
        x = move.x,
        y = move.y,
        game_id = move.game_id,
        player_id = player_id
    )
    db.add(db_user_move)
    db.commit()
    db.refresh(db_user_move) 
    return db_user_move

def check_winner(board: list, symbol: str):

    for row in board:
        if row[0] == row[1] == row[2] == symbol:
            return True
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    
    return False
        
def get_board(db: Session, game_id: int, player_id: int):
    board = [['.' for _ in range(3)] for _ in range(3)]
    for move in get_moves_by_game(db, game_id):
        board[move.x][move.y] = 'X' if move.player_id == player_id else 'O'
    
    return board