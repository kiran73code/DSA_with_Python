from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        if head == None :
            return head 

        while( n > 0):
            if(fast.next == None ):
                head = slow.next
                return head
            fast = fast.next
            n -= 1
       
        while(fast.next != None):
            slow = slow.next
            fast = fast.next

        if slow.next == fast:
            slow.next = None
            return head
            
        if slow.next.next != None:
            slow.next = slow.next.next
        

        return head
    

    
if __name__ == "__main__":
    def traverse(head):
        print(head.val)
        while head.next != None:
            head = head.next
            print(head.val)
            
            
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    head1 = s.removeNthFromEnd(head, 2)
    traverse(head1)
   
 
        

        