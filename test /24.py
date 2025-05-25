def merge_in_place(arr1, m, arr2, n):
    i = m - 1          # pointer at last valid element in arr1
    j = n - 1          # pointer at last element in arr2
    k = m + n - 1      # pointer at end of arr1 (write location)

    # Merge while both arrays have items left
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:       # if arr1 has the bigger element
            arr1[k] = arr1[i]       # put it at the end
            i -= 1                  # move arr1 pointer back
        else:
            arr1[k] = arr2[j]       # arr2 has the bigger element
            j -= 1                  # move arr2 pointer back
        k -= 1                      # move write pointer back

    # If anything left in arr2, copy it
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
