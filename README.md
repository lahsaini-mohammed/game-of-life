This is a simple visualization of Conway's Game of Life in the terminal.

This implementation includes:

- A GameOfLife class that handles the game logic
- Random initialization of the grid
- Proper handling of edge cases using wrap-around
- Clear visualization in the terminal
- Main game loop with animation

To run the game:

- Make sure you have NumPy installed (pip install numpy)
- Save the code and run it
- The game will start automatically with a random initial state
- Press Ctrl+C to stop the game

The game uses:

- '■' for live cells
- '□' for dead cells

The rules of Conway's Game of Life are implemented as follows:

- Any live cell with fewer than 2 live neighbors dies (underpopulation)
- Any live cell with 2 or 3 live neighbors lives on
- Any live cell with more than 3 live neighbors dies (overpopulation)
- Any dead cell with exactly 3 live neighbors becomes alive (reproduction)