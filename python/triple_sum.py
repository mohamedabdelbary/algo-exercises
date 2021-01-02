def triple_sum(li, k):
    """
    Given an array of numbers and a number k, determine if there are three entries in the array which add up to the
    specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
    """
    if len(li) < 3:
        return False
    if len(li) == 3:
        return sum(li) == k

    li = sorted(li)
    for i in range(len(li) - 2):
        j = i + 1
        z = len(li) - 1
        while j < z:
            sum_ = li[i] + li[j] + li[z]
            if sum_ == k:
                return True
            elif sum_ < k:
                j += 1
            else:
                z -= 1
    return False


if __name__ == "__main__":
    assert triple_sum([20, 303, 3, 4, 25], 49) is True
    assert triple_sum([20, 303, 3, 4, 25], 1) is False
    assert triple_sum([20, 303, 3, 4, 25], 4) is False
    assert triple_sum([20, 303, 3, 4, 25], 9) is False
    assert triple_sum([20, 303, 3, 4, 25], 310) is True
