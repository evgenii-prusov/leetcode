from node import ListNode


def print_linked_list(head: ListNode):
    while head:
        print(head, end='->')
        head = head.next
    print()


def to_string(head: ListNode):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next

    return "".join(result)