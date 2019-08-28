class Queue:
    def __init__(self,list = None):
        if(list == None):
            self.items = []
        else:
            self.items = list
    def size(self):
        return len(self.items)
    def enQ(self,x):
        self.items.append(x)
    def deQ(self):
        if(self.size() >0):
            return self.items.pop(0)
        else:
            return "Queue is Empty"
    def isEmpty(self):
        return self.size() == 0 

q= Queue()
print(q.isEmpty())
q.enQ(1)
print(q.isEmpty())
q.enQ(2)
print(q.size())
print(q.items)
print(q.deQ())

