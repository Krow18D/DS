class Stack:
    def __init__(self,list_=None):
        if(list_ == None):
            self.items = []
        else:
            self.items = list_
    def size(self):
        return len(self.items)
    def push(self,x):
        self.items.append(x)
    def pop(self):
        if(self.size()>0):
            return self.items.pop()
    def peek(self):
        return self.items[-1]
    def __str__(self):
        out =""
        for i in self.items:
            out+=i
        return out
class Queue:
    def __init__(self,list_=None):
        if(list_ == None):
            self.items = []
        else:
            self.items = list_
    def size(self):
        return len(self.items)
    def enQ(self,x):
        self.items.append(x)
    def deQ(self):
        if(self.size()>0):
            return self.items.pop(0)
    def __str__(self):
        out =""
        for i in self.items:
            out+=i
        return out
def reverseS(stack):
    q= Queue()
    while(stack.size()>0):
        q.enQ(stack.pop())
    while(q.size()>0):
        stack.push(q.deQ())

    
    
l = [c for c in input("input: ").split()]
print("l = ",l)
s=Stack(l)
print(s)
reverseS(s)
print(s)
