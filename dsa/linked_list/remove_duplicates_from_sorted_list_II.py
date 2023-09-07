from typing import Optional

from node import ListNode
from utils import to_string


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty or single node linked list
        if not head or not head.next:
            return head

        left: ListNode = head
        right: ListNode = head
        prev: Optional[ListNode] = None
        while right.next:
            right = right.next
            # duplicates detected, go to the next iteration
            if left.val == right.val:
                continue
            if left.next.val == right.val:
                prev = left
                left = left.next
                continue

            while left.val != right.val:
                # prev = left
                if left.val == head.val:
                    head = head.next
                    prev = left
                left = left.next
                # prev.next = None
            if head.val == left.val:
                prev.next = None

            prev.next = left

        # in case if only one node left
        if not head.next:
            return head
        # in case if two duplicates left
        if head.val == right.val:
            return None

        if left.next and left.val == right.val:
            prev.next = None

        return head


def test_delete_duplicates_first_three_of_five_node_are_duplicates():
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(1), ListNode(1), ListNode(2), ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1, r2 = ListNode(2), ListNode(3)
    r1.next = r2
    expected: str = to_string(r1)

    assert result == expected


def test_delete_duplicates_three_nodes_all_duplicates():
    n1, n2, n3 = ListNode(1), ListNode(1), ListNode(1)
    n1.next = n2
    n2.next = n3
    result: str = to_string(Solution().deleteDuplicates(head=n1))

    expected: str = ''

    assert result == expected


def test_delete_duplicates_first_three_and_second_two_of_five_nodes_are_duplicates():
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(1), ListNode(1), ListNode(2), ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result: str = to_string(Solution().deleteDuplicates(head=n1))

    expected: str = ''

    assert result == expected


def test_delete_duplicates_four_nodes_last_three_are_duplicates():
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(2), ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1 = ListNode(1)
    expected: str = to_string(r1)

    assert result == expected


def test_delete_duplicates_seven_nodes_and_two_groups_of_duplicates_in_the_middle():
    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n4, n5, n6 = ListNode(3), ListNode(4), ListNode(4)
    n7 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    result: str = to_string(Solution().deleteDuplicates(head=n1))

    r1, r2, r3 = ListNode(1), ListNode(2), ListNode(5)
    r1.next = r2
    r2.next = r3
    expected: str = to_string(r1)

    assert result == expected
