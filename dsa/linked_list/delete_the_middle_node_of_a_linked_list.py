from typing import Optional

from node import ListNode
from utils import to_string


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        if not head.next.next:
            head.next = None
            return head

        origin_head: ListNode = head
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        slow.next = None

        return origin_head


def test_delete_middle_1():
    n1 = ListNode(1)

    assert Solution().deleteMiddle(head=n1) is None


def test_delete_middle_2():
    n1, n2 = ListNode(1), ListNode(2)
    n1.next = n2

    r1 = ListNode(1)
    expected = to_string(r1)
    result = to_string(Solution().deleteMiddle(head=n1))

    assert result == expected


def test_delete_middle_3():
    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n1.next = n2
    n2.next = n3

    r1, r3 = ListNode(1), ListNode(3)
    r1.next = r3
    expected = to_string(r1)
    result = to_string(Solution().deleteMiddle(head=n1))

    assert result == expected


def test_delete_middle_4():
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    r1, r2, r4 = ListNode(1), ListNode(2), ListNode(4)
    r1.next = r2
    r2.next = r4
    expected = to_string(r1)
    result = to_string(Solution().deleteMiddle(head=n1))

    assert result == expected


def test_delete_middle_5():
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    r1, r2, r4, r5 = ListNode(1), ListNode(2), ListNode(4), ListNode(5)
    r1.next = r2
    r2.next = r4
    r4.next = r5
    expected = to_string(r1)
    result = to_string(Solution().deleteMiddle(head=n1))

    assert result == expected


def test_delete_middle_6():
    n1, n2, n3 = ListNode(1), ListNode(3), ListNode(4)
    n4, n5, n6 = ListNode(7), ListNode(1), ListNode(2)
    n7 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    r1, r2, r3 = ListNode(1), ListNode(3), ListNode(4)
    r5, r6, r7 = ListNode(1), ListNode(2), ListNode(6)
    r1.next = r2
    r2.next = r3
    r3.next = r5
    r5.next = r6
    r6.next = r7
    expected = to_string(r1)
    result = to_string(Solution().deleteMiddle(head=n1))

    assert result == expected
