def is_max_heap(arr):
    """
    Checks if a given array represents a max heap.

    Args:
        arr: The array to check.

    Returns:
        True if the array is a max heap, False otherwise.
    """
    n = len(arr)
    # Check for each non-leaf node if it satisfies the max heap property
    for i in range(n // 2 - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2

        # If left child exists and is greater than parent
        if left < n and arr[left] > arr[i]:
            return False

        # If right child exists and is greater than parent
        if right < n and arr[right] > arr[i]:
            return False
    return True

# Test cases
test_cases = [
    [8, 7, 6, 4, 2, 3, 5, 1],  # True (from previous insertion example)
    [10, 5, 3, 2, 4],  # True
    [10, 5, 3, 6, 4],  # False (6 is greater than its parent 3)
    [1, 2, 3, 4, 5],   # False
    [1],  # True
    [],   # True
    [5,3,8] # False
]

for arr in test_cases:
    print(f"Array {arr} is max heap: {is_max_heap(arr)}")
