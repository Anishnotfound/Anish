def quicksort(arr):
    if len(arr) <= 1:
        return arr  # base case: if the array is of length 1 or empty, it's already sorted
    pivot = arr[0]  # choose the first element as the pivot
    left = [x for x in arr[1:] if x <= pivot]  # elements less than or equal to pivot
    right = [x for x in arr[1:] if x > pivot]  # elements greater than the pivot
    return quicksort(left) + [pivot] + quicksort(right)  # recursive calls to sort left and right

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)
