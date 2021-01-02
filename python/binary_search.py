def binary_search(li, x):
    """
    Given a sorted list li, return the index at which x appears using binary search
    i.e. in O(log(N)) time complexity where N is the length of li.

    If x is not in the list, return -1.

    :param li: list of sorted elements
    :param x: element to search for
    :return:
    """
    if not li:
        return -1
    if len(li) == 1:
        return 0 if li[0] == x else -1

    mid_idx = len(li) // 2
    if x < li[mid_idx]:
        return binary_search(li[:mid_idx], x)
    else:
        idx = binary_search(li[mid_idx:], x)
        return (mid_idx + idx) if idx > -1 else -1


if __name__ == "__main__":
    assert binary_search([1, 2, 3, 4], 4) == 3
    assert binary_search([1, 2, 3, 4], 3) == 2
    assert binary_search([], 10) == -1
    assert binary_search([2, 7, 8], 10) == -1
    assert binary_search([1, 2, 3, 4], 2) == 1
    assert binary_search(["a", "b", "c", "z"], "x") == -1
    assert binary_search(["a", "b", "c", "z"], "c") == 2
    assert binary_search([1, 2, 2.5, 3, 4], 1) == 0
