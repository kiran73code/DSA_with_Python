class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
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
    
    def moveToHead(self, temp):
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

        self.addToHead(temp)
    
    def removeTail(self):
        if(self.tail.prev!=None):
            self.tail.prev.next=None
        else:
            self.head = None

        self.map.pop(self.tail.key)
        self.tail = self.tail.prev
    

    def get(self, key: int) -> int:
        if(key in self.map):
            temp = self.map.get(key)
            self.moveToHead(temp)
            return temp.value

        return -1
        

    def put(self, key: int, value: int) -> None:
        temp = self.Node()
        if(key in self.map): 
            temp = self.map.get(key)
            temp.value = value
            self.moveToHead(temp)
        else:
            if(len(self.map)>=self.capacity):
                self.removeTail()
            temp =  self.Node(key,value)
            self.map[key]= temp
            self.addToHead(temp)
        

if __name__ == "__main__":
# Your LRUCache object will be instantiated and called as such:

    obj = LRUCache(5)
    print(obj.get(1))
    obj.put(1,"one")
    print( obj.get(1))