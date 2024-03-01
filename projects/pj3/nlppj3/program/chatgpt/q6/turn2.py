
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if len(self.stack1) == 0:
            raise IndexError("Queue is empty!")
        return self.stack1.pop()

    def peek(self):
        if len(self.stack1) == 0:
            raise IndexError("Queue is empty!")
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0

    def size(self):
        return len(self.stack1)


# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())  # Output: 2
print(q.size())  # Output: 2
print(q.is_empty())  # Output: False
