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

    def addNode(self, val):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def removeTail(self):
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    def removeNode(self, val):
        curr = self.head
        while curr.next.val != val:
            curr = curr.next
        curr.next = curr.next.next

    def getHead(self):
        curr = self.head
        return curr.val
    
    def getTail(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.val
    
if __name__ == "__main__":
	x = Node(10);
	llist = LinkedList(x)
	llist.addNode(20)
	llist.addNode(30)
	llist.addNode(40)
	llist.visualize()
	print(llist.getHead());
	print(llist.getTail());
	llist.removeTail();
	llist.removeNode(20);
	llist.visualize()
