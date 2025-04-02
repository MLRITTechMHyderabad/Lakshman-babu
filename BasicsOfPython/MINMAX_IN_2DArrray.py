arr = [[1,2,3],
       [4,5,6],
       [7,10,23]]
# for i in arr:
#     print(i)

# max_ele = max(map(max, arr))
# min_ele = min(map(min, arr))

# print("Max element of 2D array:", max_ele)
# print("Min element of 2D array:", min_ele)

print("Min:", min(min(row) for row in arr), "Max:", max(max(row) for row in arr))