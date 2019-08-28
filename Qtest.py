class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQ(self,x):
        self.items.append(x)
    def deQ(self):
        if len(self.items) >0:
            return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
q=Queue()
print(q.isEmpty())
q.enQ(1)
q.enQ(2)
q.enQ(3)
print(q.items)
q.deQ()
print(q.items)
print(q.size())
print(q.isEmpty())
