"""Given a list of non-negative integers, arrange them such that they form the largest possible number.
Return the result as a string."""

def largest_number(nums):
    # Convert numbers to strings
    nums_str = list(map(str, nums))

    n = len(nums_str)
    # Bubble sort with custom compare
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                # Swap
                nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]

    result = ''.join(nums_str)

    # Handle leading zeros like "000" → "0"
    return '0' if result[0] == '0' else result

# ✅ Test Cases
print(largest_number([10, 2]))          # "210"
print(largest_number([3, 30, 34, 5, 9]))# "9534330"
print(largest_number([0, 0]))            # "0"
