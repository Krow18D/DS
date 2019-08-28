class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items=[]
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else :
            return False

    def pop(self):
        if len(self.items)>0:
            self.items.pop()
        else:
            print("you can't pop anymore Stack is EMPTY")

    def peek(self):
        return self.items[len(self.items)-1]

s= Stack()
print(s.isEmpty())
s.push(7)
s.push(3)
s.push(4)
print(s.size())
print(s.isEmpty())
print(s.items)
s.pop()
print(s.items)
print(s.peek())
s.pop()
print(s.items)
s.pop()
print(s.items)
s.pop()





