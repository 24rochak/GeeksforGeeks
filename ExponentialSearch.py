from BinarySearch import binary_search


def exponential_search(arr: [int], key: int):
    """
    Performs exponential search over given array.
    Performs great in unbounded array and when element to be searched is closer to starting index.
    Time complexity : O(log(n))
    :param arr: Sorted input array.
    :param key: Value to be found out.
    :return: Index of key if it is present in the array else -1.
    """

    # Calculate the length of array.
    n = len(arr)

    # Check if first element matches the key.
    if arr[0] == key:
        return 0;

    # Find index i where arr[i] > key.
    i = 1;
    while i < n and arr[i] <= key:
        i = i * 2

    # Perform binary search over the target array.
    return binary_search(arr, key, int(i / 2), min(i, n - 1))


if __name__ == '__main__':
    # Test array
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    key = 42

    # Perform interpolation_search
    loc = exponential_search(arr, key)

    # Display the index of key
    print("Key is present at index : ", loc)
