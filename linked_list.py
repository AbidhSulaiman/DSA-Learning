
"""
* travelling function
* insert new node
* delete node

"""

class singlyNode:
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
class singlyNode1:
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)

class LinkedList():
    
    def __init__(self, head = None, prev = None):
        self.head = head
        self.prev = prev
    
    def printHead(self):
        print(self.head)
        
    def travell(self, head):
        temp = head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
            
    def last(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp.val
    
    def insertBig(self, val):
        new_node = singlyNode(val)
        temp = self.head
        
        new_node.next = temp
        self.head = new_node
        
    def insertLast(self, val):
        
        new_node = singlyNode(val)
        temp = self.head
        
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def insertafter(self, cuval, val):
        new_node = singlyNode(val)
        temp = self.head
        while temp.next:
            if temp.val == cuval:
                next_val = temp.next
                temp.next = new_node
                new_node.next = next_val
            temp = temp.next
            
    def reverse(self, head):
        current = head
        prev = self.prev
        
        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        return prev
        
        
    def ditectCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
    
    """
    1) 1-2-5-7
    2) 3-4-6-8
    res) 1-2-3-4-5-6-7-8
    """   
    def merge(self, head1,head2):
        temp1 = head1
        temp2 = head2
        prev = None
        
        while temp1 and temp2:
            if temp2.val > temp1.val:
                prev = temp1
                temp1 = temp1.next
            else:
                cur = temp1
                cur2 = temp2
                prev.next = cur2
                cur2.next = cur
                temp2 = temp2.next
        


Head = singlyNode(1)
A = singlyNode(2)
B = singlyNode(5)
C = singlyNode(7)

Head.next = A
A.next = B
B.next = C

Head1 = singlyNode(3)
E = singlyNode(4)
F = singlyNode(6)
G = singlyNode(8)

Head1.next = E
E.next = F
F.next = G


l = LinkedList(Head)
l.merge(Head,Head1)

# print(l.ditectCycle(Head))
l.travell(Head)
# l.insertafter(2,3)
# new_head = l.reverse(Head)
# l.travell(new_head)



    


