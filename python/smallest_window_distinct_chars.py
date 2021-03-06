def smallest_window_distinct_chars(s):
    """
    This problem was asked by Amazon.

    Given a string, find the length of the smallest window that contains every distinct character.
    Characters may appear more than once in the window.

    For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
    """

    # TODO: This solution is O(N^2). Look into optimising.
    if len(s) == 1:
        return 1
    char_set = set(s)
    shortest = len(s) + 1
    for i in range(len(s)):
        found_chars = set()
        curr_seq_len = 0
        for j in range(i, len(s)):
            c = s[j]
            found_chars.add(c)
            curr_seq_len += 1
            if found_chars == char_set:
                if curr_seq_len < shortest:
                    shortest = curr_seq_len
    return shortest


if __name__ == "__main__":
    assert smallest_window_distinct_chars("jiujitsu") == 5
    assert smallest_window_distinct_chars("jiujiiu") == 3
    assert smallest_window_distinct_chars("abcabc") == 3
    assert smallest_window_distinct_chars("aaaaaaa") == 1
    assert smallest_window_distinct_chars("abcdef") == 6
    assert smallest_window_distinct_chars("opportunity") == 9
    assert smallest_window_distinct_chars("opportunit") == 7
    assert smallest_window_distinct_chars("amusement") == 9
