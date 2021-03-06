def balanced_parentheses(s) -> bool:
    unmatched_open = 0
    for c in s:
        if c == ")":
            if unmatched_open == 0:
                return False
            unmatched_open -= 1
        elif c == "(":
            unmatched_open += 1
    return unmatched_open == 0


if __name__ == "__main__":
    assert balanced_parentheses(")(") is False
    assert balanced_parentheses(")") is False
    assert balanced_parentheses("(") is False
    assert balanced_parentheses("(((") is False
    assert balanced_parentheses("()") is True
    assert balanced_parentheses("(kfdli)") is True
    assert balanced_parentheses("((()))") is True
    assert balanced_parentheses("(((|x)))") is True
    assert balanced_parentheses("((())))") is False
    assert balanced_parentheses("(((|))))") is False
    assert balanced_parentheses("((()))(") is False
    assert balanced_parentheses("()(())") is True
    assert balanced_parentheses("()(())(") is False
    assert balanced_parentheses("()(())(abc)") is True
