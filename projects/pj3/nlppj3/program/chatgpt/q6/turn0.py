
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "Queue is empty"
        
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
    
    def front(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "Queue is empty"

        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        return len(self.stack1) + len(self.stack2)
