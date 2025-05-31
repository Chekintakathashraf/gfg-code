# Best for clarity and interviews
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


print(insert_interval([[1,3], [6,9]], [2,5]))
# Output: [[1,5], [6,9]]

print(insert_interval([[1,2], [3,5], [6,7], [8,10], [12,16]], [4,8]))
# Output: [[1,2], [3,10], [12,16]]
