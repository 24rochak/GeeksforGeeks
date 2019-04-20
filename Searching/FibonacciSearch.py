def fib_search(arr: [int], key: int):
    """
    Performs Fibonacci Search over given input array.
    :param arr: Input array.
    :param key: Value to be found out.
    :return: Index of key if it is present else -1
    """

    # Initialise the variables.
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib0 = fib1 + fib2
    offset = -1

    # Find the index such that it is the smallest number greater than the key.
    while fib2 < n:
        fib2 = fib1
        fib1 = fib0
        fib0 = fib1 + fib2

    # While only a single element is left for comparison.
    while fib1 > 1:

        # Find index to compare the values.
        i = min(fib2 + offset, n-1)

        # If key < arr[index], shift fibonacci to 2 values down,
        # Eliminating 2/3 of the right array.
        if key < arr[i]:
            fib0 = fib2
            fib1 = fib1 - fib0
            fib2 = fib2 - fib1

        # If key > arr[index], shift fibonacci to 1 values down,
        # Eliminating 1/3 of the left array.
        elif key > arr[i]:
            fib0 = fib1
            fib1 = fib2
            fib2 = fib0 - fib1
            offset = i

        # If key == arr[index], return index.
        else:
            return i

    # Only single element left, if key==arr[last element], return last element.
    if fib1 == 1 and arr[offset+1] == key:
        return offset+1

    # Element not present, return -1.
    else :
        return -1



if __name__ == '__main__':
    # Test Array.
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    key = 34

    # Perform fibonacci search
    loc = fib_search(arr, key)

    # Display the location of key.
    print("Element found at loc : ",loc)
