class Node:
    """node creation"""

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class DoublyLinkedList:
    """doubly linked list"""
    
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    head = Node()
    head = n1
    n1.next = n2
    while (head is not None):
        print(head.data)
        head = head.next