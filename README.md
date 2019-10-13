# scopa-ai

## Status
The game logic is finalized and I'm working on the main loop of the game. Another important step is the format of 
the display for each round. After the coding of the game is finished, I'm going to work on playing startegies. Below is 
a list of strategies to be implemented.
 
## Proposed playing strategies
- v0: randomized moves
- v1: rule based approach

## How to play
To make a move enter the index of the card you want to play and the indices of cards on the table separated by spaces
- Example:

        Player 1: (clubs, 5) (spades, 9) (cups, 7) 
        Table: (coins, 2) (clubs, 3) (cups, 5) (coins, 8) 
        Player 2: (clubs, 10) (coins, 4) (cups, 1)

Player one uses (cups, 7) to take (coins, 2) and (cups, 5): `2 0 2`