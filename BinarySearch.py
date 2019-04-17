def binary_search(arr: [int], key: int, low: int, high: int):
    """
    Performs binary search over given array.
    Time complexity : O(log(n))
    :param arr: Sorted Input Array.
    :param key: Value to be found out.
    :param low: Starting index of Array.
    :param high: Ending index of Array.
    :return: Index of key if it is present in array else -1.
    """

    # Check if array is valid or not.
    if low <= high:
        # Find index of middle element.
        mid = int((low + high) / 2)

        if arr[mid] == key:
            # Return index of key if it is present.
            return mid

        elif arr[mid] > key:
            # Perform binary search over left sub array if middle element is greater than key.
            return binary_search(arr, key, low, mid - 1)

        else:
            # Perform binary search over right sub array if middle element is smaller than key.
            return binary_search(arr, key, mid + 1, high)
    else:
        # Return -1 as element is not present.
        return -1


if __name__ == '__main__':
    # Test array.
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    key = 50

    # Perform binary search.
    loc = binary_search(arr, key, 0, len(arr) - 1)

    # Display the location of key.
    print("Found at location : ", loc)