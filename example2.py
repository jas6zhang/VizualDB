from debugger import debug


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    node = head
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    debug(reverse_list, (head,))
