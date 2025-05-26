def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # overlap
            last[1] = max(last[1], current[1])  # merge
        else:
            merged.append(current)

    return merged

print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))
# Output: [[1,6], [8,10], [15,18]]

print(merge_intervals([[1,4],[4,5]]))
# Output: [[1,5]]
