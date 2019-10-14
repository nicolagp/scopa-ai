# scopa-ai

## Status
The game logic is finalized and I'm working on the main loop of the game. Another important step is the format of 
the display for each round. After the coding of the game is finished, I'm going to work on playing startegies. Below is 
a list of strategies to be implemented.

## To do
- Extend funtion that checks valid moves to include the case of trying to put card with a match on table 
- Think of a better way of displaying the game
- Corner case: round ends, figure out who to give the remaining cards to

## Proposed playing strategies
- Random Moves
- Rule Based
- Monte Carlo Tree Search
- Minimax

## How to play
To make a move enter the index of the card you want to play and the indices of cards on the table separated by spaces
- Example:

        Player 1: (clubs, 5) (spades, 9) (cups, 7) 
        Table: (coins, 2) (clubs, 3) (cups, 5) (coins, 8) 
        Player 2: (clubs, 10) (coins, 4) (cups, 1)

Player one uses (cups, 7) to take (coins, 2) and (cups, 5): `2 0 2`