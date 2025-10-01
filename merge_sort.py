def merge_sort(arr):
    if len(arr) <= 1:   # base case
        return arr
    
    # find middle index
    mid = len(arr) // 2

    # recursively split into left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # compare elements from left and right arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
