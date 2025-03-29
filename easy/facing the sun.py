"""def countBuildings(height):
    if not height:
        return 0  # Edge case: empty array

    count = 1  # First building always sees the sunrise
    max_height = height[0]

    for h in height[1:]:
        if h > max_height:
            count += 1
            max_height = h  # Update the tallest building so far

    return count

# Example Test Cases
print(countBuildings([7, 4, 8, 2, 9]))  # Output: 3
print(countBuildings([2, 3, 4, 5]))  # Output: 4
print(countBuildings([5, 5, 5, 5]))  # Output: 1 (only the first building sees the sun)
"""


def countBuildings(height):
    

    count = 1  # First building always sees the sunrise
    max_height = height[0]

    for h in height[1:]:
        if h > max_height:
            count += 1
            max_height = h  # Update the tallest building so far

    return count

# Example Test Cases
print(countBuildings([7, 4, 8, 2, 9]))  # Output: 3
print(countBuildings([2, 3, 4, 5]))  # Output: 4
print(countBuildings([5, 5, 5, 5]))  # Output: 1 (only the first building sees the sun)
