from typing import Optional

from node import ListNode
from utils import to_string


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = fast = origin_head = head
        for i in range(n-1):
            fast = fast.next

        prev = None
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        if not prev:
            return slow.next
        prev.next = slow.next
        slow.next = None

        return origin_head


def test_remove_nth_from_end_1():
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result = to_string(Solution().removeNthFromEnd(head=n1, n=2))

    r1, r2, r3, r5 = ListNode(1), ListNode(2), ListNode(3), ListNode(5)
    r1.next = r2
    r2.next = r3
    r3.next = r5
    expected = to_string(r1)

    assert result == expected


def test_remove_nth_from_end_2():
    n1 = ListNode(1)

    assert Solution().removeNthFromEnd(head=n1, n=1) is None


def test_remove_nth_from_end_3():
    n1, n2 = ListNode(1), ListNode(2)
    n1.next = n2
    result = to_string(Solution().removeNthFromEnd(head=n1, n=1))

    r1 = ListNode(1)
    expected = to_string(r1)

    assert result == expected


def test_remove_nth_from_end_4():
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result = to_string(Solution().removeNthFromEnd(head=n1, n=4))

    r1, r3, r4, r5 = ListNode(1), ListNode(3), ListNode(4), ListNode(5)
    r1.next = r3
    r3.next = r4
    r4.next = r5
    expected = to_string(r1)

    assert result == expected


def test_remove_nth_from_end_5():
    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n1.next = n2
    n2.next = n3
    result: str = to_string(Solution().removeNthFromEnd(head=n1, n=3))

    r2, r3 = ListNode(2), ListNode(3)
    r2.next = r3
    expected: str = to_string(r2)

    assert result == expected


def test_remove_nth_from_end_6():
    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n1.next = n2
    n2.next = n3
    result: str = to_string(Solution().removeNthFromEnd(head=n1, n=1))

    r1, r2 = ListNode(1), ListNode(2)
    r1.next = r2
    expected: str = to_string(r1)

    assert result == expected
