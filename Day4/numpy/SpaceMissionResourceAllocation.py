import numpy as np

# (6,3) array
resources = np.array([
    [15, 40, 32], 
    [20, 42, 35], 
    [25, 38, 30], 
    [18, 50, 40], 
    [22, 37, 36], 
    [28, 45, 33] 
])

total_resources = np.sum(resources, axis=0)
print(f"Total resources needed (tons): Oxygen: {total_resources[0]}, Water: {total_resources[1]}, Food: {total_resources[2]}")

# Highest consumption in month (row-wise max)
max_monthly_value = np.max(resources)
max_month_index = np.argmax(resources)
row, col = divmod(max_month_index, 3)

resource_names = ["Oxygen", "Water", "Food"]
print(f"Highest consumption in a month: {resource_names[col]} ({resources[row][col]} tons in month {row + 1})")

# Standard deviation 
std_devs = np.std(resources, axis=0)
print(f"Standard deviation of consumption: Oxygen: {std_devs[0]:.1f}, Water: {std_devs[1]:.1f}, Food: {std_devs[2]:.1f}")

#Transposed matrix
transposed = resources.T
print("Transposed matrix:")
print(transposed)
