🎬 Movie Recommender System
✅ Description
This Python application uses the IMDb Top 1000 movies dataset to recommend movies based on:

🎭 Genre

📅 Release year (specific or range)

⭐ Minimum IMDb rating

It features:

Modern neon-themed GUI using Tkinter

Poster previews using PIL and image URLs

Scrollable recommendations and autosuggestions while typing

🧠 Tech Stack
Python, Pandas

Tkinter for GUI

PIL for image handling

IMDb dataset (CSV)

▶️ How to Run
Make sure the IMDb dataset CSV path is correctly set in the code.

Run the script with any Python IDE or terminal.

Input preferred Genre, Year or Year Range, and IMDb rating.

Click 🎯 Recommend to see results.

Click 📩 More Suggestions for additional movies.

🖼️ Output Example
![image](https://github.com/user-attachments/assets/294a1508-80ce-4a96-8833-1bb8c25cfa47)

The GUI displays:

Movie posters

Title, Year, Genre, Rating

Neon color-themed modern interface with input suggestions

❌🎮 Tic-Tac-Toe with Minimax AI
✅ Description
This classic Tic-Tac-Toe game lets a human player play against an AI using the Minimax algorithm. The AI always plays optimally.

🤖 Features
Minimax-based AI (unbeatable)

Tkinter GUI with 3x3 grid

Reset and Game-over prompts (Win, Lose, Draw)

🧠 Algorithm Used
Minimax (no pruning) for perfect play

Evaluates best possible move for AI ('O')

Human is 'X', plays first

▶️ How to Run
Run the script in Python.

Click cells to play your move.

The AI will automatically respond.

Message boxes declare winner or draw.

Board resets after each game.

🖼️ Output
![image](https://github.com/user-attachments/assets/0d43269c-05d7-42ff-8575-60e709e1c070)
![image](https://github.com/user-attachments/assets/da4f5130-d26b-49ec-9a6d-bfa177df0ee1)


A 3x3 button grid

Player's and computer's moves appear as 'X' and 'O'

Pop-up alerts declare game result and restart the game

📂 File Structure
plaintext
Copy
Edit
├── imdb_top_1000.csv        # Required dataset for Movie Recommender
├── movie_recommender.py     # Contains full movie recommendation GUI logic
├── tic_tac_toe_minimax.py   # Contains full AI-based Tic-Tac-Toe game logic
├── README.md                # This file
