class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
        
    def enqueue(self, item)-> None:
        if self.size == self.capacity:
            print("queue is full ")
            return -1
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.size += 1
            print("item enqueued")
    
    def dequeue(self):
        if self.size == 0:
            print("queue is empty")
            return -1
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            print("item dequeued")
            return item