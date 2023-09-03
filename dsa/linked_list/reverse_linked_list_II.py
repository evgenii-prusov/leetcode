from typing import Optional
from node import ListNode
from utils import print_linked_list


class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        orig_head = left_head = left_tail = central_head = central_tail = right_head = head
        if left == 1:
            left_head = left_tail = None
            central_head = head

        pos = 1
        while head:
            if pos == left - 1:
                left_tail = head
                central_head = head.next
            if pos == right:
                central_tail = head
                right_head = head.next
                central_tail.next = None
            head = head.next
            pos += 1

        # reversing of intreval
        head = central_head
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        central_head.next = right_head

        if not left_head:
            return prev
        else:
            left_tail.next = prev
            return left_head

def test_reverse_between_1():
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    r1, r2, r3, r4, r5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    r1.next = r4
    r4.next = r3
    r3.next = r2
    r2.next = r5
    expected = r1

    print_linked_list(Solution().reverseBetween(head=n1, left=2, right=4))
    # assert Solution().reverseBetween(head=n1, left=2, right=4) == expected


def test_reverse_between_2():
    assert Solution().reverseBetween(head=[5], left=1, right=1) == [5]


def test_reverse_between_3():
    n1, n2 = ListNode(1), ListNode(2)
    n1.next = n2

    r1, r2 = ListNode(1), ListNode(2)
    r2.next = r1
    assert Solution().reverseBetween(head=n1, left=1, right=2) == r2


def test_reverse_between_4():
    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n1.next = n2
    n2.next = n3
    r1, r2, r3 = ListNode(1), ListNode(2), ListNode(3)
    r2.next = r1
    r1.next = r3
    print_linked_list(Solution().reverseBetween(head=n1, left=1, right=2))
    # assert Solution().reverseBetween(head=n1, left=1, right=2) == r2


def test_reverse_between_5():
    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n1.next = n2
    n2.next = n3
    r1, r2, r3 = ListNode(1), ListNode(2), ListNode(3)
    r1.next = r2
    r2.next = r3
    print_linked_list(Solution().reverseBetween(head=n1, left=2, right=2))
    # assert Solution().reverseBetween(head=n1, left=2, right=2) == r1


def test_reverse_between_6():
    n1, n2, n3, n4, n5, n6 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    r1, r2, r3, r4, r5, r6 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
    r1.next = r2
    r2.next = r3
    r3.next = r5
    r5.next = r4
    r4.next = r6

    print_linked_list(Solution().reverseBetween(head=n1, left=4, right=5))
    # assert Solution().reverseBetween(head=n1, left=4, right=5) == r1
