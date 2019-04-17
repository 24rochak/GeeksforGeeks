def interpolation_search(arr: [int], key: int, low: int, high: int) -> int:
    """
    Performs Interpolation Search over given array. Works best when elements are uniformly distributed.
    Time complexity : O(log(log(n))), worst case : O(n)
    :param arr: Sorted Input Array.
    :param key: Value to be searched for.
    :param low: Starting index of target array.
    :param high: Ending index of target array.
    :return: Index of key if it is present in the array else -1.
    """

    # Check if array is valid or not.
    if low <= high:

        # If corners are reached, to avoid division by 0 error, check here itself.
        if low == high:
            if arr[low] == key :
                # Return index of low if key is present.
                return low;

            return -1;

        # Calculate location of pos.
        pos = low + int(((key - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if arr[pos] == key:
            # Return index of pos if key is present.
            return pos;
        elif arr[pos] > key:
            # Perform interpolation_search on left sub-array.
            return interpolation_search(arr, key, low, pos - 1)
        else:
            # Perform interpolation_search on right sub-array.
            return interpolation_search(arr, key, pos + 1, high)
    else:
        return -1


if __name__ == '__main__':
    # Test array
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    key = 33

    # Perform interpolation_search
    loc = interpolation_search(arr, key, 0, len(arr) - 1)

    # Display the index of key
    print("Key is present at index : ", loc)
