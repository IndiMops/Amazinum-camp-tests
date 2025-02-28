import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate a random 20x20 matrix
matrix = np.random.randint(0, 2, (20, 20))
print("The initial matrix:\n", matrix)

# Uncomment the following lines to create a glider gun pattern in the top left corner
# glider_gun = [
#     (5, 1), (5, 2), (6, 1), (6, 2),
#     (5, 11), (6, 11), (7, 11), (4, 12), (8, 12), (3, 13), (9, 13), (3, 14), (9, 14),
#     (6, 15), (4, 16), (8, 16), (5, 17), (6, 17), (7, 17), (6, 18),
#     (3, 21), (4, 21), (5, 21), (3, 22), (4, 22), (5, 22), (2, 23), (6, 23),
#     (1, 25), (2, 25), (6, 25), (7, 25),
#     (3, 35), (4, 35), (3, 36), (4, 36)
# ]
# for (x, y) in glider_gun:
#     matrix[x, y] = 1
# print("Initial matrix with glider gun pattern:\n", matrix)

def game_of_life_step(board):
    new_board = board.copy()
    rows, cols = board.shape
    for i in range(rows):
        for j in range(cols):
            neighbors = board[max(i - 1, 0):min(i + 2, rows), max(j - 1, 0):min(j + 2, cols)]
            total = np.sum(neighbors) - board[i, j]
            if board[i, j] == 1:
                if total < 2:
                    new_board[i, j] = 0
                elif total > 3:
                    new_board[i, j] = 0
                else:
                    new_board[i, j] = 1
            else:
                if total == 3:
                    new_board[i, j] = 1
                else:
                    new_board[i, j] = 0
    return new_board


steps = int(input("Enter the number of steps: "))
boards = [matrix]
current_board = matrix
for step in range(steps):
    current_board = game_of_life_step(current_board)
    boards.append(current_board)

print("Matrix after {} steps:\n".format(steps), boards[-1])

fig, ax = plt.subplots()
cax = ax.matshow(boards[0], cmap='Greys')
ax.set_title("Step 0")

def update(frame):
    ax.clear()
    ax.matshow(boards[frame], cmap='Greys')
    ax.set_title(f"Step {frame}")

ani = animation.FuncAnimation(fig, update, frames=len(boards), interval=500)
plt.show()
