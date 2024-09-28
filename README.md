
# Hangman Game

A simple word guessing game built with React.js for the frontend and Django for the backend. The player needs to guess the letters of a randomly selected word within a limited number of incorrect guesses.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Django Setup](#django-setup)
- [API Endpoints](#api-endpoints)


## Features

- Start a new game with a random word.
- Guess letters and receive immediate feedback.
- Displays the current game state (In Progress, Won, Lost).
- User-friendly interface with error handling.

## Technologies Used

- **Frontend**: React.js
- **Backend**: Django
- **Database**: SQLite (or your choice of database)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dileep048/hangman_game.git
   cd hangman_game
   ```

## Django Setup


1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the Django server:
   ```bash
   python manage.py runserver
   ```
   The server will start at `http://localhost:8000`. 

## API Endpoints

### Start a New Game

- **URL**: `/game/new/`
- **Method**: POST
- **Response**: 
  ```json
  {
    "game_id": 1
  }
  ```

### Get Game State

- **URL**: `/game/<id>/`
- **Method**: GET
- **Response**: 
  ```json
  {
    "id": 11,
    "status": "InProgress",
    "display_word": "b_____",
    "incorrect_guesses": 2,
    "incorrect_guesses_left": 1
  }
  
  ```

### Guess a Letter

- **URL**: `/game/<id>/guess/`
- **Method**: POST
- **Body**: 
  ```json
  {
    "letter": "P"
  }
  ```
- **Response**: 
  ```json
  {
    "correct": false,
    "game_state": {
        "id": 11,
        "status": "InProgress",
        "display_word": "b_____",
        "incorrect_guesses": 2,
        "incorrect_guesses_left": 1
    }
  }
  ```

# Running the ReactJS Project (Local)
## Setup

1. **Navigate to the `frontend` directory:**

   ```bash
   cd frontend
   npm install
   npm start


## Usage

- Access the game through your web browser at `http://localhost:3000` (after starting the React app).
- Click on "Start New Game" to begin.
- Enter a letter and click "Guess" or press the Enter key to make a guess.

