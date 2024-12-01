""" Stack and Queue Data Structures in Python """

"""
1. Stack
    A stack is a linear data structure that follows the LIFO (Last In, First Out) principle.
    The last element added to the stack is the first to be removed.
    
    Common operations in a stack include:

        Push: Add an element to the top of the stack.
        Pop: Remove the top element from the stack.
        Peek/Top: View the top element without removing it.
        IsEmpty: Check if the stack is empty.

"""

# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        """Add an element to the stack."""
        self.stack.append(val)

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)

    def display(self):
        """Display the stack."""
        print("Stack (Top -> Bottom):", self.stack[::-1])


# Example Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Output: Stack (Top -> Bottom): [30, 20, 10]
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.is_empty())  # Output: False
stack.display()  # Output: Stack (Top -> Bottom): [20, 10]


"""
2. Queue

    A queue is a linear data structure that follows the FIFO (First In, First Out) principle.
    The first element added to the queue is the first to be removed.
    
    Common operations in a queue include:

        Enqueue: Add an element to the end of the queue.
        Dequeue: Remove the front element from the queue.
        Front: View the front element without removing it.
        IsEmpty: Check if the queue is empty.

"""
# Queue Implementation


from collections import deque

class Queue:
    def __init__(self):
        """Initialize an empty queue using deque."""
        self.queue = deque()

    def enqueue(self, val):
        """Add an element to the end of the queue."""
        self.queue.append(val)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None
        return self.queue.popleft()

    def front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    def rear(self):
        """Return the rear element without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[-1]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)

    def display(self):
        """Display the queue."""
        print("Queue (Front -> Rear):", list(self.queue))


# Example Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Output: Queue (Front -> Rear): [10, 20, 30]
print("Dequeued:", queue.dequeue())  # Output: Dequeued: 10
print("Front:", queue.front())  # Output: Front: 20
print("Rear:", queue.rear())  # Output: Rear: 30
queue.display()  # Output: Queue (Front -> Rear): [20, 30]
print("Queue size:", queue.size())  # Output: Queue size: 2
print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False
