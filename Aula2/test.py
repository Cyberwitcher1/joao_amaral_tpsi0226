import time
import random

WIDTH, HEIGHT = 50, 15
CHARS = " .:-=+*#%@"
grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

try:
    while True:
        # 1. Concentrated Fuel Source (Middle of the bottom row)
        center = WIDTH // 2
        for x in range(center - 3, center + 4):
            grid[HEIGHT-1][x] = len(CHARS) - 1

        # 2. Slow Propagation with "Tapering"
        for y in range(HEIGHT - 1):
            for x in range(WIDTH):
                # Calculate drift toward the center to create a point
                if x < center: drift = random.randint(0, 1)
                elif x > center: drift = random.randint(-1, 0)
                else: drift = random.randint(-1, 1)

                src = grid[y+1][x]
                new_x = (x + drift) % WIDTH
                
                # Higher cooling rate makes the fire "shorter"
                cooling = random.randint(1, 4) 
                grid[y][new_x] = max(0, src - cooling)

        # 3. Render
        output = ["\033[H"] # Clear screen escape code
        for row in grid:
            output.append("".join(CHARS[val] for val in row).center(WIDTH))
        
        print("\n".join(output))
        time.sleep(0.15) # Slower delay for a "lazy" fire
except KeyboardInterrupt:
    print("\nCampfire extinguished.")