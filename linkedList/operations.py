from linkedList import mainLL


class Operations:
    """all linkedlist operations"""
    def __init__(self) -> None:
        pass
    
    def traverse(self, head: mainLL.Node) -> None:
        """Iterates through the Linkedlist"""
        while head is not None:
            print(head.data)
            head = head.next
    
    def insert_at_beg(self, head: mainLL.Node, data: int) -> mainLL.Node:
        """create new node and head.next is first node pointed this to new node"""
        new_node = mainLL.Node(data)
        new_node.next = head.next
        head = new_node
        return head
    
    def insert_at_end(self, head: mainLL.Node, data: int) -> mainLL.Node:
        """Insert a new node at the end of the"""
        new_node = mainLL.Node(data)
        while head.next is not None:
            head = head.next
        head.next = new_node
        return head
    
    def insert_at_random(self, head: mainLL.Node, data: int, pos: int)->mainLL.Node:
        """serach position and insert the node"""
        
        
        