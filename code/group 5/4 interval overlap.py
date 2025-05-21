"""You are given an array of meeting time intervals intervals, where each interval is represented as [start, end].
Determine if a person can attend all meetings, meaning no meetings overlap."""


def can_attend_all_meetings(intervals):
    if not intervals:
        return True

    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Check for overlaps
    for i in range(1, len(intervals)):
        prev_end = intervals[i-1][1]
        curr_start = intervals[i][0]
        if curr_start < prev_end:
            return False
    return True

# ✅ Test Cases
print(can_attend_all_meetings([[0,30],[5,10],[15,20]]))  # False
print(can_attend_all_meetings([[7,10],[2,4]]))            # True
print(can_attend_all_meetings([[1,5],[5,6]]))             # True
print(can_attend_all_meetings([[3,6],[4,5]]))             # False

