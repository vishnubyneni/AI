def clean_grid(grid):
    movements = []
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'D':
                movements.extend(['DOWN'] * i if i > 0 else [])
                movements.extend(['RIGHT'] * j if j > 0 else [])
                movements.extend(['UP'] * i)
                movements.extend(['LEFT'] * j)
                grid[i][j] = 'C'
    return movements

if __name__ == "__main__":
    grid = [['C', 'D', 'D'], ['D', 'C', 'D'], ['D', 'D', 'C']]
    movements = clean_grid(grid)
    print("Movements to clean the grid:")
    print(movements)
