class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def print_liked_list(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print()


if __name__ == '__main__':
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n1.next = n2
    n2.next = n3
    head = n1

    print_liked_list(head)
    reversed_head = reverse_linked_list(n1)
    print_liked_list(reversed_head)
