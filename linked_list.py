class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node
    
    def visualize(self):
        curr = self.head
        print(curr.val)
        while curr.next:
            print('->' + str(curr.next.val))
            curr = curr.next