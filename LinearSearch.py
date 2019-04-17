def linear_search(arr: [int], key: int) -> int:
    """
    Performs linear search over a given array.
    Time complexity : O(n)
    :param arr: Input Array.
    :param key: Integer to be found out.
    :return: Index of key if it is present in array else -1.
    """

    # Iterate over the whole array
    for i in range(0, len(arr)):
        if key == arr[i]:
            # Return index if key is present.
            return i
    # Return -1 if key not found.
    return -1


if __name__ == '__main__':
    # Test Array.
    arr = [40, 50, 60, 90, 10, 20]
    key = 100;

    # Perform linear search.
    loc = linear_search(arr, key)

    # Display the location of key.
    print("Element preent at loc : {}".format(loc))