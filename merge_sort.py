from random import randint


def _merge(left, right):
    if not left:
        return right
    if not right:
        return left

    left_pointer, right_pointer = 0, 0
    merged = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            merged.append(left[left_pointer])
            left_pointer += 1
        else:
            merged.append(right[right_pointer])
            right_pointer += 1

    if left_pointer < len(left):
        merged += left[left_pointer:]

    if right_pointer < len(right):
        merged += right[right_pointer:]

    return merged


def merge_sort(li):
    """
    Given a list li, return the list sorted in ascending order using merge sort.
    The sorting operation should have O(nlog(n)) time complexity, where n is the
    size of list li

    :param li: list of elements to sort
    :return:
    """
    if not li or len(li) == 1:
        return li
    if len(li) == 2:
        return [li[0], li[1]] if li[0] < li[1] else [li[1], li[0]]

    left = merge_sort(li[:len(li) // 2])
    right = merge_sort(li[len(li) // 2:])

    return _merge(left, right)


if __name__ == "__main__":
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert merge_sort([1, 3, 4, 2]) == [1, 2, 3, 4]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
    assert merge_sort([8, 2, 2, 7]) == [2, 2, 7, 8]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    # Test scaling
    li = [randint(0, 100000) for _ in range(100000)]
    li = merge_sort(li)
    for i in range(0, len(li) - 1):
        assert li[i + 1] >= li[i]

