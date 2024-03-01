
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.is_empty():
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())
            return self.stack1.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
