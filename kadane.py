def kadane(arr):
    max_current = max_global = arr[0]
    
    for x in arr[1:]:
        # either take current element alone OR extend the previous subarray
        max_current = max(x, max_current + x)
        
        # update global maximum
        if max_current > max_global:
            max_global = max_current
    
    return max_global


# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Array:", arr)
print("Maximum Subarray Sum:", kadane(arr))
