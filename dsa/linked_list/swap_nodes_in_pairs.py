from node import ListNode
from utils import print_linked_list
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        final_head: ListNode = head.next
        prev = None

        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head
            next_node = head.next.next
            head.next.next = head
            head.next = next_node
            head = next_node

        return final_head


if __name__ == '__main__':
    n1, n2, n3, n4, n5, n6 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    # n5.next = n6

    print_linked_list(n1)
    new_head = Solution().swapPairs(n1)
    print_linked_list(new_head)