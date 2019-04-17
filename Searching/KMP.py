def create_LPS(pattern: [str]) -> [int]:
    """
    Creates Longest prefix string for the given input pattern
    :param pattern: Input pattern
    :return: Array containing length for longest prefix for each character in the pattern.
    """

    # Convert string to character array.
    arr = list(pattern)

    # Initialize the pointers.
    i = 1
    j = 0
    m = len(arr)

    # Initialize the LPS array.
    LPS = [0] * m
    LPS[0] = 0

    # Iterate over the whole pattern.
    while i < m:

        # If characters at pointer locations do not match
        if arr[i] != arr[j]:

            # If no prior repetition is present in the pattern.
            if j == 0:
                LPS[i] = j
                i += 1

            # Begin checking again from location of last repetition.
            else:
                j = LPS[j - 1]

        # If characters at pointer location match,
        # Increment both pointers to continue matching the repetition.
        elif arr[i] == arr[j]:
            LPS[i] = j + 1
            i += 1
            j += 1


if __name__ == '__main__':
    create_LPS("aaabaaab")
