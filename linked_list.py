"""
Singly Linked List:
----------------------

A Singly Linked List is a data structure where each node contains:
    Data: The value stored in the node.
    Next Pointer: A reference to the next node in the sequence.
    
Advantages:
    * Dynamic size (no pre-allocation of memory needed).
    * Easy insertion and deletion from the front.
    
Disadvantages:
    * Cannot traverse backward.
    * Accessing a specific element takes O(n) time.

"""
class SinglyNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        new_node = SinglyNode(val)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, val):
        new_node = SinglyNode(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.val == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.val != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Key not found")
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        temp = self.head
        while temp:
            if temp.val == key:
                return True
            temp = temp.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("NULL")

sll = SinglyLinkedList()
sll.insert_at_beginning(3)
sll.insert_at_end(5)
sll.insert_at_beginning(1)
sll.traverse()  # Output: 1 -> 3 -> 5 -> NULL
sll.reverse()
sll.traverse()  # Output: 5 -> 3 -> 1 -> NULL
print(sll.search(3))  # Output: True
sll.delete_node(3)
sll.traverse()  # Output: 5 -> 1 -> NULL


"""
Doubly Linked List:
------------------------
A Doubly Linked List is a data structure where each node contains:
    Data: The value stored in the node.
    Next Pointer: A reference to the next node in the sequence.
    Previous Pointer: A reference to the previous node in the sequence.
    
Advantages:
    * Allows traversal in both directions.
    * Easier to delete nodes when compared to singly linked lists.

Disadvantages:
    * Requires more memory for the extra pointer.
    * Slightly more complex to implement.

"""

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        new_node = DoublyNode(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, val):
        new_node = DoublyNode(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, key):
        temp = self.head
        while temp:
            if temp.val == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next
        print("Key not found")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.val == key:
                return True
            temp = temp.next
        return False

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("NULL")

    def traverse_backward(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.prev
        print("NULL")

dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_end(5)
dll.insert_at_beginning(1)
dll.traverse_forward()  # Output: 1 -> 3 -> 5 -> NULL
dll.traverse_backward()  # Output: 5 -> 3 -> 1 -> NULL
print(dll.search(3))  # Output: True
dll.delete_node(3)
dll.traverse_forward()  # Output: 1 -> 5 -> NULL
