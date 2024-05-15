
# ethyca-tic-tac-toe

This project implements a REST API for playing Noughts and Crosses (Tic-tac-toe) against a computer opponent. The API allows users to create new games, make moves, and view game history according with the [Ethyca Technical Challenge -- Open Source Engineer (Python)](https://github.com/ethyca/python-takehome-2).

This solution was create using FastAPI as a framework and using a memory database just to the dev and initial test implementation.
## Installation

Install the project using python [3.11.3](https://www.python.org/downloads/release/python-3113/)

### 1. Install dependencies

```bash
  pip install -r requirements.txt
```

### 2. Export OS variable for the database 

```bash
For Unix 
    export HOST_CONNECTION="sqlite:///./db.db"

For Windows
    set HOST_CONNECTION="sqlite:///./db.db"

```

### 3. Execute db migrations

```bash
  alembic upgrade head
```

This command's going to create the tables on the database and populate the players table with the CPU player as the first record so the CPU player will have the id=1.


### 4. Execute the server

```bash
  uvicorn app.api.main:app --host=0.0.0.0 --port=8000
```

Then you can access to http://0.0.0.0:8000 and check the project


## API Reference

FastAPI offers a swagger integration to check all the API documentation, if you want to check the swagger from the API you can go to http://0.0.0.0:8000/docs

#### Create a player

```http
  POST /player
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. You need assign a unique username |

#### List all games for a player

```http
  GET /player/${player_id}/games
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `player_id`  | `int` | **Required**. Id of the player |

#### Create a game

```http
  POST /game
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `player_id`  | `int` | **Required**. Id of the player to start the game |


#### List all moves on a game

```http
  GET /game/${game_id}/moves
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `game_id`  | `int` | **Required**. Id of the game to show all moves |

#### Create a move
```http
  GET /move
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `x`  | `int` | **Required**. Postion on the matrix, between 0 and 2 |
| `y`  | `int` | **Required**. Postion on the matrix, between 0 and 2 |
| `game_id`  | `int` | **Required**. Id of the game to asign the move |
| `player_id`  | `int` | **Required**. Id of the player who makes the move |






## Deployment

To deploy you can use docker to run the image on your local without follow all the installation steps.

### 1. Build the image

```bash
  docker build -t ethyca_tic_tac_toe .
```

### 2. Run the image

```bash
  docker run -d -p 8000:8000 ethyca_tic_tac_toe
```

Then you can go to http://localhost:8000/docs to check the local deployment

## Project summary

### Time Spent

I spent approximately 3 hours building this project and almost 1 hour create de documentation.

### Assumptions

-  CPU player always is the fist player on the players table.
- Random moves by the computer opponent are sufficient for gameplay.
- The game board is represented as a 3x3 grid.
- Players can only make moves on empty spaces on the board.
- Memory database is enought for this implementation.
- No test covage is needed.

### Trade-offs

- No authentication or user management.
- No games for user vs user.
- Memory database.

### Feedback

The task was challenging and enjoyable. It provided an opportunity to demonstrate my problem-solving skills using Python and REST APIs. I appreciate the opportunity and look forward to discussing the project further in the debrief interview.