def linear_search(arr, target):
    # Loop through each element with its index
    for index, value in enumerate(arr):

        # Check if current value matches target
        if value == target:
            return index  # Return index if found

    # Return -1 if target does not exist
    return -1


numbers = [4, 9, 2, 7, 5]

result = linear_search(numbers, 7)

print("Index:", result)