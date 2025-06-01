def fun(arr, k):
    max_sum = current_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# arr = [1, 9, -1, -2, 7, 3]
# k = 4

arr = [2,1,5,1,3,2]
k = 3

print(fun(arr, k))  

