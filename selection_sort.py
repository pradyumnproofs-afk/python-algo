def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # assume the first element of the unsorted part is the minimum
        
        # find the index of the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = selection_sort(arr[:])  # use arr[:] to keep original array intact
print("Sorted array:", sorted_arr)
