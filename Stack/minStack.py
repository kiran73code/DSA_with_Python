class MinStack:

    def __init__(self):
        self.s = []
        self.min = -1
        

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            self.min = val
            self.s.append(val)
        else:
            if val <= self.min:
                new_val = (2*val-self.min)
                self.min = val
                self.s.append(new_val)
            else:
                self.s.append(val)
        

    def pop(self) -> None:
        if len(self.s) == 0:
            return None
        else:
            val = self.s[-1]
            if  val <= self.min:
                self.min = (2*self.min - val)
                return self.s.pop()
            else:
                return self.s.pop()


    def top(self) -> int: 
        if len(self.s) == 0:
            return None  
        if self.s[-1] <= self.min :
            return self.min
        else:
            return self.s[-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.top())
print(obj.getMin())