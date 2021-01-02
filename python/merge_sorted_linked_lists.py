class Node:
    def __init__(self, value):
        self._value = value
        self.next = None

    @property
    def value(self):
        return self._value

    def as_list(self):
        li = []
        n = self
        while n:
            li.append(n.value)
            n = n.next
        return li


def merge_sorted_linked_lists(head_1, head_2):
    if not head_1:
        return head_2
    elif not head_2:
        return head_1
    if head_1.value < head_2.value:
        head_1.next = merge_sorted_linked_lists(head_1.next, head_2)
        return head_1
    else:
        head_2.next = merge_sorted_linked_lists(head_1, head_2.next)
        return head_2


if __name__ == "__main__":
    l_1_head = Node(1)
    l_1_head.next = Node(2)
    l_1_head.next.next = Node(4)

    l_2_head = Node(1)
    l_2_head.next = Node(3)
    l_2_head.next.next = Node(5)
    assert merge_sorted_linked_lists(l_1_head, l_2_head).as_list() == [1, 1, 2, 3, 4, 5]
