class WavefrontPlanner:
    # (unchanged code...)

    def visualize_grid(self, wavefront_grid):
        # Print the wavefront grid for visualization
        for row in wavefront_grid:
            print(row)

# Example usage:
grid_map = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (4, 0)
goal = (0, 4)

planner = WavefrontPlanner(grid_map)
path = planner.plan_path(start, goal)

# Visualize the wavefront grid
planner.visualize_grid(wavefront_grid)

# Print the path
print("Path:", path)
