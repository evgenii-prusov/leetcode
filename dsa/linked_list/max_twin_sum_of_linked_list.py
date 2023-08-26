from node import ListNode
from utils import print_linked_list
from typing import Optional


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s = f = head
        prev = None
        i = 0

        while f and f.next:
            if prev:
                prev = prev.next
            else:
                prev = s
            s = s.next
            f = f.next.next

            i += 1

        middle: ListNode = s
        if f:
            middle = s.next
            prev = prev.next
            i += 1

        curr = middle
        prev2 = None
        while curr:
            next_node = curr.next
            curr.next = prev2
            prev2 = curr
            curr = next_node

        prev.next = prev2

        s = f = head
        for _ in range(i):
            f = f.next

        max_sum = 0
        while f:
            curr_sum = s.val + f.val
            max_sum = max(max_sum, curr_sum)
            s = s.next
            f = f.next

        return max_sum


if __name__ == '__main__':
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    print_linked_list(n1)
    print(Solution().pairSum(n1))

    n01, n02, n03, n04, n05 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n01.next = n02
    n02.next = n03
    n03.next = n04
    n04.next = n05

    print_linked_list(n01)
    print(Solution().pairSum(n01))
