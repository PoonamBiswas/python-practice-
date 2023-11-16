class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue (self, item):
        self.enqueue.append(item)

    def dequeue (self):
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack)>0:
                item = self.enqueue_stack.pop()
                self.dequeue_stack.append(item)
        if len(self.dequeue_stack) == 0:
            return None
    def is_empty(self):
        return len(self.enqueue_stack)==0 and len(self.dequeue_stack)
    def size(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)
