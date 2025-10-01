def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # element to be placed in the correct position
        j = i - 1
        
        # shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # place key at its correct position
        arr[j + 1] = key

    return arr


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = insertion_sort(arr[:])  # use arr[:] to keep original array intact
print("Sorted array:", sorted_arr)
