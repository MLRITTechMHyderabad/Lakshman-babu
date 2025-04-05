import numpy as np

points = np.array([
    [10, 25, 30, 22, 12, 18, 26, 32, 24, 29],
    [20, 15, 12, 28, 24, 26, 30, 18, 22, 25],
    [35, 30, 32, 40, 28, 34, 29, 31, 26, 37],
    [12, 18, 20, 15, 22, 14, 19, 21, 23, 17],
    [28, 26, 27, 25, 30, 29, 35, 32, 31, 38]
])

# average points per player
avg_points = np.mean(points, axis=1)
print("Average points per game:")
print(avg_points)

# Best and Worst players 
total_points = np.sum(points, axis=1)
best_index = np.argmax(total_points)
worst_index = np.argmin(total_points)

print(f"\nBest-performing player: Player {best_index + 1} (Total: {total_points[best_index]} points)")
print(f"Worst-performing player: Player {worst_index + 1} (Total: {total_points[worst_index]} points)")


print("\nGames with scores above 30:")
for i in range(points.shape[0]):
    high_scores = np.where(points[i] > 30)[0]
    if len(high_scores) > 0:
        print(f"Player {i + 1}: Games {[x + 1 for x in high_scores]}")

#Sort players by total points
sorted_indices = np.argsort(total_points)[::-1]  # descending
print("\nSorted Players by Total Points:")
for rank, idx in enumerate(sorted_indices, start=1):
    print(f"{rank}. Player {idx + 1} - {total_points[idx]} points")
