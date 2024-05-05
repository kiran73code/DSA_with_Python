class Stack
    def __init__(self):
        self.s = []
        self.size = 0
    
    def push(self, val:int)->None:
        self.s.append(val)
        self.size += 1
    
    def pop(self)->None:
        if self.size > 0:
            self.size -= 1
            self.s.pop()
        else:
            raise "stack is empty"
        
    def peek(self)->int:
        if self.size > 0:
            return self.s[-1]
        else:
            raise "stack is empty"


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
        
