def max_subarray_sum(a):
    """
    Given an array of integers a, find the consecutive subarray with the maximum sum in a
    e.g. a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    should return a sum of 43 ([18, 20, -7, 12])

    e.g., given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
    42, 14, -5, and 86.

    Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
    """
    max_idx_sum = {}
    for idx, e in enumerate(a):
        if idx == 0:
            max_idx_sum[idx] = e
        else:
            sub = a[0: idx]
            sum_ = sum(sub)
            max_ = sum_
            start = 0
            while start < idx:
                if sum_ > max_:
                    max_ = sum_
                sum_ -= a[start]
                start += 1
            max_with_curr = max_ + e
            max_idx_sum[idx] = e if e > max_with_curr else max_with_curr
    max_sum = max(max_idx_sum.values())
    return max_sum if max_sum > 0 else 0


if __name__ == "__main__":
    assert max_subarray_sum([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]) == 43
    assert max_subarray_sum(range(1, 5)) == 10
    assert max_subarray_sum([1, 2, 3, 4, -1]) == 10
    assert max_subarray_sum([34, -50, 42, 14, -5, 86]) == 137
    assert max_subarray_sum([-5, -1, -8, -9]) == 0
