def create_LPS(pat: [str], m: int) -> [int]:
    """
    Creates Longest prefix string for the given input pattern.
    Time complexity : O(m)
    :param pattern: Input pattern
    :return: Array containing length for longest prefix for each character in the pattern.
    """

    # Initialize the pointers.
    i = 1
    j = 0

    # Initialize the LPS array.
    LPS = [0] * m
    LPS[0] = 0

    # Iterate over the whole pattern.
    while i < m:

        # If characters at pointer locations do not match.
        if pat[i] != pat[j]:

            # If no prior repetition is present in the pattern.
            if j == 0:
                LPS[i] = j
                i += 1

            # Begin checking again from location of last repetition.
            else:
                j = LPS[j - 1]

        # If characters at pointer location match,
        # Increment both pointers to continue matching the repetition.
        else:
            LPS[i] = j + 1
            i += 1
            j += 1
    return LPS


def findOccurrences(text: str, pattern: str) -> [int]:
    """
    Finds the occurrences of pattern in a given string.
    Time complexity : O(m+n)
    :param string: Input string where pattern is to be searched for.
    :param pattern: Pattern which is to be searched.
    :return: Array of indices which point to the location where pattern is present.
    """

    # Convert pattern to character array.
    pattern = list(pattern)
    m = len(pattern)

    # Obtain the Largest Prefix String(LPS) Array.
    LPS = create_LPS(pattern, m)
    # print("LPS is : ",LPS)

    # Convert string into character array.
    text = list(text)
    n = len(text)

    # Initialise the pointers.
    i = 0  # Pointer for text
    j = 0  # Pointer for LPS array.
    indices = []

    # Iterate over the whole array.
    while i < n:
        # If characters at pointer location match,
        # Increment both pointers to continue matching the repetition.
        if text[i] == pattern[j]:
            i += 1
            j += 1

        # If characters do not match.
        else:
            # Point j to the previous repetition.
            if j != 0:
                j = LPS[j - 1]
            # If repetition is not present (j=0), increment the text pointer.
            else:
                i += 1

        # If full pattern is matched.
        if j == m:
            # Point j to the previous repetition.
            j = LPS[j - 1]
            # Add index of beginning to matched indices.
            indices.append(i - m)
    # Return list of indices.
    return indices


if __name__ == '__main__':
    # Test Data.
    string = "AABAACAADAABAABA"
    pattern = "AABA"

    # Perform KMP search.
    loc = findOccurrences(string, pattern)

    # Display the indices where pattern is present in string.
    print("Pattern matched at indices : ", loc)