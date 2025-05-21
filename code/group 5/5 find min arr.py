"""You are given a list of balloons as intervals: each balloon is represented as [start, end], the horizontal diameter.
One arrow can burst all balloons that overlap with the point where it’s shot.

Return the minimum number of arrows needed to burst all balloons."""


def find_min_arrow_shots(points):
    if not points:
        return 0

    # Step 1: Sort by end of balloons
    points.sort(key=lambda x: x[1])

    arrows = 1
    last_arrow_pos = points[0][1]

    # Step 2: Greedy loop
    for start, end in points[1:]:
        if start > last_arrow_pos:
            arrows += 1
            last_arrow_pos = end

    return arrows

# ✅ Test Cases
print(find_min_arrow_shots([[10,16],[2,8],[1,6],[7,12]]))  # 2
print(find_min_arrow_shots([[1,2],[3,4],[5,6],[7,8]]))      # 4
print(find_min_arrow_shots([[1,2],[2,3],[3,4],[4,5]]))      # 2
print(find_min_arrow_shots([[1,10]]))                      # 1

