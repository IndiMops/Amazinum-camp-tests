import random

import matplotlib.pyplot as plt

# 1. Generate 20 random values
values = [random.randint(0, 100) for _ in range(20)]
print("Generated values:", values)

# 2. Function to find the deepest lake depth
def deepest_lake_depth(values):
    n = len(values)
    max_depth = 0
    best_pair = None  # store the indices of the left and right boundaries of the lake
    # Iterate through all pairs of indices with at least one element between them
    for i in range(n - 1):
        for j in range(i + 2, n):
            # Check if all values between i and j are smaller than both end values
            if all(values[k] < values[i] for k in range(i + 1, j)) and all(values[k] < values[j] for k in range(i + 1, j)):
                water_level = min(values[i], values[j])  # water level is the minimum of the two ends
                lake_bottom = min(values[k] for k in range(i + 1, j))  # lowest point of the lake
                depth = water_level - lake_bottom
                if depth > max_depth:
                    max_depth = depth
                    best_pair = (i, j)
    return max_depth, best_pair

depth, best_pair = deepest_lake_depth(values)
print("The deepest depth of the lake:", depth)
print("Lake boundaries indices:", best_pair)

# 3. Visualize the sequence and highlight the lake
plt.figure(figsize=(10, 5))
plt.plot(range(len(values)), values, marker='o', label='Heights')

if best_pair is not None:
    i, j = best_pair
    water_level = min(values[i], values[j])
    # Highlight the area between i and j
    x_vals = list(range(i, j + 1))
    y_vals = values[i:j + 1]
    plt.fill_between(x_vals, y_vals, water_level, color='skyblue', alpha=0.5, label='Deepest Lake')
    # Draw a water level line
    plt.hlines(water_level, i, j, colors='blue', linestyles='--')

plt.title("The heights of the mountains and the deepest lake")
plt.xlabel("Index")
plt.ylabel("Height")
plt.legend()
plt.show()
