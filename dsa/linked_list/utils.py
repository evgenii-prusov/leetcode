from node import ListNode


def print_linked_list(head: ListNode):
    while head:
        print(head, end='->')
        head = head.next
    print()
