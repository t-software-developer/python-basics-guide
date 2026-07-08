def bubble_sort(arr):
    n = len(arr)

    # Repeat passes through the list
    for i in range(n):

        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            # Swap if elements are out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(numbers))