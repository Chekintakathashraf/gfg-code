"""Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input."""

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlap
            last[1] = max(last[1], current[1])  # Merge
        else:
            merged.append(current)

    return merged

# Test
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  
# Output: [[1,6],[8,10],[15,18]]

print(merge_intervals([[1,4],[4,5]]))  
# Output: [[1,5]]
