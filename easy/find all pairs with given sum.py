"""Given two unsorted arrays a[]  and b[], the task is to find all pairs whose sum equals x from both arrays.

Note: All pairs should be returned in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then (u1,v1) should be returned first else second.

Examples:

Input: target = 9, a[] = [1, 2, 4, 5, 7], b[] = [5, 6, 3, 4, 8]
Output: 
1 8
4 5 
5 4
Explanation: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.

Input: target = 8, a[] = [-1, -2, 4, -6, 5, 7], b[] = [6, 3, 4, 0]
Output:
4 4 
5 3

Input: target = 9, a[] = [1, 2, 4, 5, 7, 4], b[] = [5, 6, 3, 4, 8, 4]
Output:
1 8
4 5
4 5
5 4
5 4
Explanation: (1, 8), (4, 5), (4, 5), (5, 4) and (5, 4) are the pairs which sum to 9."""




def all_pairs(target, arr1, arr2):
    arr1.sort()  # Ensure pairs are in increasing order of 'u'
    freq_map = {}  # Dictionary to store frequency of arr2 elements

    # Count occurrences of each element in arr2
    for num in arr2:
        freq_map[num] = freq_map.get(num, 0) + 1

    result = []
    for u in arr1:
        v = target - u
        if v in freq_map:
            for _ in range(freq_map[v]):  # Add as many times as it appears
                result.append((u, v))

    return result

# 🔹 Test Cases
print(all_pairs(9, [1, 2, 4, 5, 7, 4], [5, 6, 3, 4, 8, 4]))
# ✅ Output: [(1, 8), (4, 5), (4, 5), (5, 4), (5, 4)]
print(all_pairs(8, [-1, -2, 4, -6, 5, 7], [6, 3, 4, 0]))
# ✅ Output: [(4, 4), (5, 3)]
print(all_pairs(9, [1, 2, 4, 5, 7], [5, 6, 3, 4, 8]))
# ✅ Output: [(1, 8), (4, 5), (5, 4)]
print(all_pairs(9, [1, 2, 4, 5, 7], [5, 6, 3, 4, 8]))
# ✅ Output: [(1, 8), (4, 5), (5, 4)]

