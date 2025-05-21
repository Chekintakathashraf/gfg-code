"""You are given a list of non-overlapping intervals, sorted by start time.
You are also given a new interval to insert into the list.

Insert the interval and merge if necessary, so that the result remains sorted and non-overlapping."""

def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Step 1: Add intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Step 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Step 3: Add the rest
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# ✅ Test Cases
print(insert_interval([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]
print(insert_interval([], [5,7]))  # [[5,7]]
print(insert_interval([[1,5]], [2,3]))  # [[1,5]]

