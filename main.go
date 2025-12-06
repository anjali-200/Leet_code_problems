package main

import (
	"fmt"
	"html/template"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"time"
)

// The HTML template includes all CSS and JavaScript in one place for simplicity.
const gameHTML = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Roll (Go Game)</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background: #ffffff;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 90%;
            text-align: center;
        }
        h1 {
            color: #4CAF50;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }
        p {
            color: #666;
            margin-bottom: 2rem;
            font-size: 0.95rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #333;
        }
        select {
            width: 100%;
            padding: 10px;
            margin-bottom: 1.5rem;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-sizing: border-box;
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 0.7em top 50%;
            background-size: 0.65em auto;
        }
        button {
            background-color: #2196F3;
            color: white;
            border: none;
            padding: 12px 25px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin-top: 10px;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.3s ease, transform 0.1s;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            font-weight: 700;
            width: 100%;
        }
        button:hover {
            background-color: #1976D2;
        }
        button:active {
            transform: translateY(1px);
        }
        #result {
            margin-top: 2rem;
            padding: 1rem;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 700;
            min-height: 25px;
        }
        .win { background-color: #E8F5E9; color: #4CAF50; }
        .lose { background-color: #FFEBEE; color: #F44336; }
        .info { background-color: #E3F2FD; color: #2196F3; }

        /* Responsive Design */
        @media (max-width: 600px) {
            .container {
                padding: 2rem 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎲 Guess the Roll</h1>
        <p>Try to guess the number the Go server rolls (1 to 6). Good luck!</p>

        <label for="guess">Your Guess:</label>
        <select id="guess">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
        </select>

        <button onclick="rollDice()">Roll Dice</button>

        <div id="result" class="info">Click 'Roll Dice' to start!</div>
    </div>

    <script>
        // JavaScript function to call the Go backend
        async function rollDice() {
            const guessElement = document.getElementById('guess');
            const resultElement = document.getElementById('result');
            const userGuess = guessElement.value;

            resultElement.className = 'info';
            resultElement.textContent = 'Rolling...';

            try {
                // Send the user's guess to the Go server's API endpoint
                const response = await fetch('/api/roll?guess=' + userGuess);
                
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                
                // Update the result based on the server's response
                resultElement.textContent = data.message;
                resultElement.className = data.win ? 'win' : 'lose';

            } catch (error) {
                console.error('Fetch error:', error);
                resultElement.textContent = 'Error contacting the server.';
                resultElement.className = 'lose';
            }
        }
    </script>
</body>
</html>
`

// Struct to hold the server's response data
type RollResponse struct {
	Message string `json:"message"`
	Win     bool   `json:"win"`
}

func init() {
	// Seed the random number generator using the current time
	// This is critical for getting different results each time.
	rand.Seed(time.Now().UnixNano())
}

// indexHandler serves the main HTML page for the game.
func indexHandler(w http.ResponseWriter, r *http.Request) {
	// Execute the embedded HTML template directly
	tmpl, err := template.New("game").Parse(gameHTML)
	if err != nil {
		http.Error(w, "Could not parse HTML template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}

// rollHandler handles the game logic: rolling the dice and determining the result.
func rollHandler(w http.ResponseWriter, r *http.Request) {
	// Set the content type to JSON
	w.Header().Set("Content-Type", "application/json")

	// 1. Get the user's guess from the URL query parameter
	guessStr := r.URL.Query().Get("guess")
	if guessStr == "" {
		http.Error(w, `{"message": "Missing guess parameter", "win": false}`, http.StatusBadRequest)
		return
	}

	guess, err := strconv.Atoi(guessStr)
	if err != nil || guess < 1 || guess > 6 {
		http.Error(w, `{"message": "Invalid guess value", "win": false}`, http.StatusBadRequest)
		return
	}

	// 2. Generate the random dice roll (1 to 6)
	// rand.Intn(n) generates a number in [0, n-1], so we add 1
	roll := rand.Intn(6) + 1

	// 3. Compare the guess and the roll
	var response RollResponse

	if guess == roll {
		response = RollResponse{
			Message: fmt.Sprintf("You won! The roll was %d.", roll),
			Win:     true,
		}
	} else {
		response = RollResponse{
			Message: fmt.Sprintf("You lost. The roll was %d. Try again!", roll),
			Win:     false,
		}
	}

	// 4. Send the JSON response back to the client
	fmt.Fprintf(w, `{"message": "%s", "win": %t}`, response.Message, response.Win)
}

func main() {
	// Define the routes:
	// "/" serves the main game page
	http.HandleFunc("/", indexHandler)
	// "/api/roll" is the API endpoint where the game logic is executed
	http.HandleFunc("/api/roll", rollHandler)

	port := "8080"
	log.Printf("Starting Guess the Roll game server on http://localhost:%s", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}

