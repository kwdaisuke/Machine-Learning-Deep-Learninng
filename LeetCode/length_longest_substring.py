def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    :param s: Input string.
    :return: Length of the longest substring without repeating characters.
    """
    char_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_map:
            # Update the start position
            start = max(start, char_map[s[end]] + 1)
            print(start)
        # Update the character's latest index
        char_map[s[end]] = end
        print("map", char_map)
        # Calculate the length of the current non-repeating substring
        max_length = max(max_length, end - start + 1)
        print("max", max_length)

    return max_length

# Test the function with the provided examples
example1 = length_of_longest_substring("abcabcbb")  # Expected: 3
example2 = length_of_longest_substring("bbbbb")     # Expected: 1
example3 = length_of_longest_substring("pwwkew")    # Expected: 3

example1, example2, example3