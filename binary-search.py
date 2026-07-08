def binary_search(arr, target):
    # Define search boundaries
    left = 0
    right = len(arr) - 1

    # Continue while search space exists
    while left <= right:

        # Find middle position
        mid = (left + right) // 2

        # Target found
        if arr[mid] == target:
            return mid

        # Search right half
        elif arr[mid] < target:
            left = mid + 1

        # Search left half
        else:
            right = mid - 1

    # Target not found
    return -1


numbers = [2, 4, 6, 8, 10, 12]

print(binary_search(numbers, 10))