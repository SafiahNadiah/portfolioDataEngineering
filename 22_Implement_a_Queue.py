
class Queue:
    def __init__(self):
        self.items = []
 
    def enqueue(self, item):
        self.items.append(item)
 
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
 
    def peek(self):
        if not self.is_empty():
            return self.items[0]
 
    def is_empty(self):
        return len(self.items) == 0
 
    def size(self):
        return len(self.items)

"""
Implement a Queue
Create a class called Queue that implements a queue data structure. The queue should support the following operations:

enqueue(item): Adds an item to the back of the queue.

dequeue(): Removes and returns the item from the front of the queue.

peek(): Returns the item at the front of the queue without removing it.

is_empty(): Returns True if the queue is empty and False otherwise.

size(): Returns the number of items in the queue.

Your Queue class should use only built-in Python tools, such as lists, and should not use any external libraries or modules.



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
 
print(queue.dequeue())  # Should print 1
print(queue.peek())  # Should print 2
print(queue.is_empty())  # Should print False
print(queue.size())  # Should print 2

"""
