def jump_search(arr: [int], key: int):
    """
    Performs jump search over given array.
    Time complexity : O((n)**0.5)
    :param arr: Sorted Input Array.
    :param key: Value to be found out.
    :return: Index of key if it is present in the array else -1.
    """
    n = len(arr)

    # Calculate step size.
    step = int(len(arr) ** 0.5)

    # Initialize iterator.
    prev = 0

    # Iterate over the array until arr[step] < key.
    while arr[int(min(prev, n))] < key:
        prev = prev + step

    # If the step size is large, binary search can be performed over the target array.
    # loc = binary_search(arr,key,prev-step,prev)
    # Else perform linear search.

    # Iterate over the target array.
    for i in range(prev - step, prev):
        if arr[i] == key:
            # Return index of key if it is present in the array.
            return i
    # Return -1 as key is not present in the array.
    return -1


if __name__ == '__main__':
    # Test array
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

    # Perform jump search
    loc = jump_search(arr, 10)

    # Display the location of key.
    print("Item present at : ", loc)