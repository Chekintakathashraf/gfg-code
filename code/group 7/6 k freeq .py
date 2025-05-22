"""Given an integer array nums and an integer k, return the k most frequent elements."""

#=============== without heap

def topKFrequent(nums, k):
    from collections import defaultdict

    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    # Create buckets: index = frequency, value = list of numbers with that frequency
    max_freq = max(freq_map.values())
    bucket = [[] for _ in range(max_freq + 1)]

    for num, freq in freq_map.items():
        bucket[freq].append(num)

    result = []
    for freq in range(len(bucket) - 1, 0, -1):  # Start from high freq
        for num in bucket[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result

print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1,2]
print(topKFrequent([1], 1))           # Output: [1]
print(topKFrequent([4,1,4,4,2,2,3], 2))  # Output: [4,2]

