"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Only start at the beginning of a sequence
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]))     # Output: 4
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))      # Output: 9
print(longest_consecutive([]))                        # Output: 0

