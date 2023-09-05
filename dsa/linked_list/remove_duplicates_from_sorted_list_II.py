from typing import Optional

from node import ListNode as LNode
from utils import to_string


class Solution:
    def deleteDuplicates(self, head: Optional[LNode]) -> Optional[LNode]:
        # empty or single node linked list
        if not head or not head.next:
            return head

        prev = None
        slow = fast = head
        fast = fast.next
        while fast and fast.next:

            if slow.val == fast.val:
                # in case first two elements are equal
                if not prev:
                    new_head = head.next.next
                    head.next = None
                    head = new_head
                    slow = head
                    fast.next = None
                    fast = slow.next
                else:
                    prev.next = fast.next
                    slow = fast.next
                    fast = fast.next.next
            else:
                prev = slow
                slow = slow.next
                fast = fast.next

        if fast and slow.val == fast.val:
            if not prev:
                return None
            prev.next = None

        return head


def test_delete_duplicates_1():
    n1, n2, n3, n4, n5, n6, n7 = LNode(1), LNode(2), LNode(3), LNode(3), LNode(4), LNode(4), LNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1, r2, r3 = LNode(1), LNode(2), LNode(5)
    r1.next = r2
    r2.next = r3
    expected: str = to_string(r1)

    assert result == expected


def test_delete_duplicates_2():
    n1, n2, n3, n4, n5 = LNode(1), LNode(1), LNode(1), LNode(2), LNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1, r2, r3 = LNode(1), LNode(2), LNode(3)
    r1.next = r2
    r2.next = r3

    expected: str = to_string(r1)

    assert result == expected


def test_delete_duplicates_3():
    n1, n2, n3, n4 = LNode(1), LNode(2), LNode(3), LNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1, r2 = LNode(1), LNode(2)
    r1.next = r2

    expected: str = to_string(r1)

    assert result == expected


def test_delete_duplicates_four_equal_nodes():
    n1, n2, n3, n4 = LNode(1), LNode(1), LNode(1), LNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    result: str = to_string(Solution().deleteDuplicates(head=n1))

    expected: str = ''

    assert result == expected


def test_delete_duplicates_three_equal_nodes():
    n1, n2, n3 = LNode(1), LNode(1), LNode(1)
    n1.next = n2
    n2.next = n3

    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1 = LNode(1)
    expected: str = to_string(r1)

    assert result == expected


def test_delete_duplicates_two_equal_nodes():
    n1, n2 = LNode(1), LNode(1)
    n1.next = n2

    result: str = to_string(Solution().deleteDuplicates(head=n1))

    expected: str = ''

    assert result == expected


def test_delete_duplicates_single_node():
    n1 = LNode(1)

    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1 = LNode(1)

    expected: str = to_string(r1)

    assert result == expected


def test_delete_duplicates_no_nodes():
    n1 = None

    assert Solution().deleteDuplicates(head=n1) is None


def test_delete_duplicates_two_nodes_without_duplicates():
    n1, n2 = LNode(1), LNode(2)
    n1.next = n2

    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1, r2 = LNode(1), LNode(2)
    r1.next = r2

    expected: str = to_string(r1)

    assert result == expected
