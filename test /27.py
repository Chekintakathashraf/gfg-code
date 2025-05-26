arr = [1,9,-1,-2,7,3]

k = 4

def fun(arr,k):
    
    max_sum = current_window_sum = sum(arr[:k])
    max_start_index = 0
    
    for end_index in range(k,len(arr)):
        current_window_sum = current_window_sum + arr[end_index] - arr[end_index - k]
        
        if current_window_sum > max_sum:
            max_sum = current_window_sum
            max_start_index = end_index -k +1
        
    return max_sum , arr[max_start_index : max_start_index + k]


print(fun(arr,k))
        
        
        
        
        
        
        
        
        