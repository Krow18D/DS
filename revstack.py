class Stack:
    def __init__(self,list = None):
        if(list == None):
            self.items = []
        else:
            self.items = list
    def push(self,x):
        self.items.append(x)
    def peek(self):\
        return self.items[-1]
    def pop(self):
        if(len(self.items)>0):
            return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)

st = input()
s=Stack()
rev = Stack()
for i in st:
    s.push(i)

print(s.items)
while(s.isEmpty()==False):
    rev.push(s.pop())
print(rev.items)
