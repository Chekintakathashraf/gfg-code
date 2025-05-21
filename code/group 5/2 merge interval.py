"""    You are given a list of intervals where each interval is represented as [start, end].
    Merge all overlapping intervals and return the result as a list of merged intervals in sorted order.

 Each interval [a, b] means it starts at a and ends at b, inclusive."""

def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    # Step 2: Scan and merge
    for current in intervals[1:]:
        last = merged[-1]

        # Check for overlap
        if current[0] <= last[1]:
            # Merge by extending the end
            last[1] = max(last[1], current[1])
        else:
            # No overlap, just add it
            merged.append(current)

    return merged

# ✅ Test Cases
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))                 # [[1,5]]
print(merge_intervals([[5,7],[1,3]]))                 # [[1,3],[5,7]]
