import numpy as np
import time
import os

class GameOfLife:
    def __init__(self, width=50, height=30):
        self.width = width
        self.height = height
        self.grid = np.random.choice([0, 1], size=(height, width), p=[0.85, 0.15])
    
    def count_neighbors(self, row, col):
        # Count neighbors using slicing with wrap-around
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r = (row + i) % self.height
                c = (col + j) % self.width
                total += self.grid[r, c]
        return total
    
    def next_generation(self):
        new_grid = np.zeros((self.height, self.width))
        
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.count_neighbors(row, col)
                current_state = self.grid[row, col]
                
                # Apply Conway's Game of Life rules
                if current_state == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[row, col] = 0  # Cell dies
                    else:
                        new_grid[row, col] = 1  # Cell survives
                else:
                    if neighbors == 3:
                        new_grid[row, col] = 1  # Cell becomes alive
                    else:
                        new_grid[row, col] = 0  # Cell stays dead
        
        self.grid = new_grid
    
    def display(self):
        # Clear screen (works on both Windows and Unix-like systems)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for row in self.grid:
            print(''.join(['■' if cell else '□' for cell in row]))

def main():
    # Initialize the game
    game = GameOfLife()
    
    try:
        while True:
            game.display()
            game.next_generation()
            time.sleep(0.1)  # Add a small delay to make the animation visible
    except KeyboardInterrupt:
        print("\nGame terminated by user")

if __name__ == "__main__":
    main()
