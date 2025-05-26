# sum btw i and j

def build_prefix_sum(arr):
  
    prefix = [0] 
    for i in arr:
        prefix.append(prefix[-1] + i)
        
    return prefix

def range_sum(prefix, i, j):
    return prefix[j + 1] - prefix[i]

#      0  1  2  3  4
arr = [3, 5, 2, 8, 6]
prefix = build_prefix_sum(arr)

# prefix = [0, 3, 8, 10, 18, 24]
print("Sum from 1 to 3:", range_sum(prefix, 1, 3))  # 5 + 2 + 8 = 15
print("Sum from 0 to 4:", range_sum(prefix, 0, 4))  # 3 + 5 + 2 + 8 + 6 = 24
print("Sum from 2 to 2:", range_sum(prefix, 2, 2))  # 2

