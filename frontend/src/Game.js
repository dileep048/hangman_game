import React, { useState } from "react";
import "./App.css";

function App() {
    const [gameId, setGameId] = useState(null);
    const [gameState, setGameState] = useState(null);
    const [guessLetter, setGuessLetter] = useState("");
    const [error, setError] = useState(null);

    // Start a new game
    const startNewGame = async () => {
        try {
            const response = await fetch("/game/new/", {
                method: "POST",
            });
            const data = await response.json();
            setGameId(data.game_id);
            fetchGameState(data.game_id);
        } catch (error) {
            console.error("Error starting a new game:", error);
            setError("Failed to start a new game. Try again.");
        }
    };

    // Fetch game state
    const fetchGameState = async (id) => {
        try {
            const response = await fetch(`/game/${id}/`, {
                method: "GET",
            });
            const data = await response.json();
            console.log("Data", data)
            setGameState(data);
            console.log("ga", gameState)
            setError(null); // Clear error
        } catch (error) {
            console.error("Error fetching game state:", error);
            setError("Failed to fetch game state. Try again.");
        }
    };

    // Guess a letter
    const guessLetterHandler = async () => {
        if (!guessLetter || guessLetter.length !== 1 || !/^[a-zA-Z]$/.test(guessLetter)) {
            setError("Please enter a single letter from a-z.");
            return;
        }
        try {
            const response = await fetch(`/game/${gameId}/guess/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ letter: guessLetter }),
            });
            const data = await response.json();
            console.log("data", data)
            if (data.error) {
                setError(data.error);
            } else {
                setGameState(data.game_state);
                setGuessLetter("");
                setError(null);
            }
        } catch (error) {
            console.error("Error guessing the letter:", error);
            setError("Failed to submit your guess. Try again.");
        }
    };

    const handleKeyDown = (event) => {
        if (event.key === "Enter") {
            guessLetterHandler();
        }
    };


    return (
        <div className="container">
            <h1>Word Guessing Game</h1>
            {!gameId ? (
                <button className="start-button" onClick={startNewGame}>
                    Start New Game
                </button>
            ) : (
                <>
                    {gameState && (
                        <div className="game-info">
                            <p>Word: {gameState.display_word}</p>
                            <p>Incorrect Guesses: {gameState.incorrect_guesses}</p>
                            <p>Guesses Left: {gameState.incorrect_guesses_left}</p>
                            <p>Status: {gameState.status}</p>
                            <p>Note: Guess one letter from a-z</p>
                        </div>
                    )}
                    {gameState && gameState.status == "InProgress" && (<div className="guess-info">
                        <input
                            type="text"
                            maxLength="1"
                            value={guessLetter}
                            onChange={(e) => setGuessLetter(e.target.value)}
                            placeholder="Guess a letter"
                            className="input-letter"
                            onKeyDown={handleKeyDown} 
                        />
                        <button className="guess-button" onClick={guessLetterHandler}>
                            Click Guess
                        </button>
                    </div>)}
                    {gameState && gameState.status == "Won" && (<div>
                        <p className="won-message">You Won the Current Game</p>
                        <button className="guess-button" onClick={startNewGame}>
                            New Game
                        </button>
                    </div>)}
                    {gameState && gameState.status == "Lost" && (<div>
                        <p className="loss-message">You Lost the Current Game</p>
                        <button className="guess-button" onClick={startNewGame}>
                            Start New Game
                        </button>
                    </div>)}
                </>
            )}
            {error && <p className="error-message">{error}</p>}
        </div>
    );
}

export default App;
