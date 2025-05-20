"""Input: [1, 2, 2, 3, 4, 4, 4]
Output: 4  # Unique elements are 1,2,3,4

Input: "banana"
Output: 3  # Unique chars: b,a,n

Distinct elements means all the different or unique elements in a list, string, or array — without counting duplicates.
Example:

    List: [1, 2, 2, 3, 4, 4]

        Distinct elements are: 1, 2, 3, 4 → total 4

    String: "banana"

        Characters are: b, a, n, a, n, a

        Distinct characters: b, a, n → total 3

So distinct means unique — count each element only once, ignoring repetitions.

"""


def count_distinct_elements(arr):
    unique_elements = set(arr)
    return len(unique_elements)

print(count_distinct_elements([1, 2, 2, 3, 4, 4, 4]))  # 4
print(count_distinct_elements("banana"))               # 3
print(count_distinct_elements([]))                      # 0

