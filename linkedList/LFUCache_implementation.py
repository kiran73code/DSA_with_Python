class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.counter = dict()
        self.head = None
        self.tail = None


    class Node:
        def __init__(self,key= None, value= None):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def addToHead(self, temp):
        if(self.head == None ):
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
    
    
    def breakNodeRelation(self, temp):
        if(temp==self.head):
            return -1
        if(temp==self.tail):
            self.tail = self.tail.prev

        #break the relation
        if(temp.prev!=None):
            temp.prev.next = temp.next
        if(temp.next!=None):
            temp.next.prev = temp.prev

        temp.prev = None
        temp.next = None
        
    
    def moveToHead(self, temp):
        check = self.breakNodeRelation(temp)
        if check != -1:
            self.addToHead(temp)
    
    def removeTail(self):
        #if(self.tail.prev!=None):
        #   self.tail.prev.next=None
        #else:
        #    self.head = None
        min_value_key = min(self.counter, key=self.counter.get)
        temp = self.map.get(min_value_key)
        check = self.breakNodeRelation(temp)
       
        self.map.pop(min_value_key)
        self.counter.pop(min_value_key)
    

    def get(self, key: int) -> int:
        if(key in self.map):
            temp = self.map.get(key)
            self.moveToHead(temp)
            if (key in self.counter):
                self.counter[key] = self.counter[key] + 1
            else:
                self.counter[key] = 1
            return temp.value

        return -1
        

    def put(self, key: int, value: int) -> None:
        temp = self.Node()
        if(key in self.map): 
            temp = self.map.get(key)
            if (key in self.counter):
                self.counter[key] = self.counter[key] + 1
            else:
                self.counter[key] = 1
            temp.value = value
            self.moveToHead(temp)
        else:
            if(len(self.map)>=self.capacity):
                self.removeTail()
            temp =  self.Node(key,value)
            self.map[key]= temp
            if (key in self.counter):
                self.counter[key] = self.counter[key] + 1
            else:
                self.counter[key] = 1
            self.addToHead(temp)
            
            
            
# Your LFUCache object will be instantiated and called as such:
if __name__ == '__main__':
    obj = LFUCache(3)
    obj.put(2,2)
    obj.put(1,1)
    obj.get(2)
    obj.get(1)
    obj.get(2)
    obj.put(3,3)
    obj.put(4,4)
    obj.get(3)

 
# param_1 = obj.get(key)
# obj.put(key,value)