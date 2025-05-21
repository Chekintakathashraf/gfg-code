"""Given an integer array nums and an integer k, return the k most frequent elements.

You must solve it in O(n log n) time or better."""

# ================ heap ==============

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq_map = Counter(nums)
    return [item for item, count in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

# Test cases
print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(top_k_frequent([1], 1))           # Output: [1]

# ============== without heap ===================

from collections import Counter

def top_k_frequent(nums, k):
    # Step 1: Count frequencies
    freq_map = Counter(nums)
    
    # Step 2: Create buckets (size = len(nums) + 1)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Step 3: Fill the buckets
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Step 4: Collect top k frequent from buckets (from high to low freq)
    result = []
    for freq in range(len(buckets) - 1, 0, -1):  # start from highest freq
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

# 🔍 Test Cases
print(top_k_frequent([1,1,1,2,2,3], 2))   # Output: [1,2]
print(top_k_frequent([1], 1))            # Output: [1]
