class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,x):
        self.items.append(x)
    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else :
            return False
    def peek(self):
        return self.items[-1]

class Narrow:
    maxcar = 4
    redpark = Stack()
    park = Stack()
    def arrive(self,car):
        if self.park.size() < self.maxcar:
            self.park.push(car)
            print("car  %d arrive    space left %d"%(car,self.maxcar-self.park.size()))
        else:
            print("car %d cannot arrive : SOI FULL" % car)

    def depart(self,car):
        if car in self.park.items:
            while car != self.park.peek():
                print("pop %d " % self.park.peek())
                self.redpark.push(self.park.pop())
            print("Car %d depart"%(self.park.pop()))
            while (self.redpark.isEmpty() == False):
                print("push %d " % self.redpark.peek())
                self.park.push(self.redpark.pop())
            print("space letf %d" % (self.maxcar - self.park.size()))
        else:
            print("car %d is not arrive"%car)





n = Narrow()
n.depart(6)
n.arrive(1)
n.arrive(2)
n.arrive(3)
n.arrive(4)
n.arrive(5)

print(n.park.items)
n.depart(2)
print("remaining car"+str(n.park.items))
n.depart(3)
print("remaining car"+str(n.park.items))
n.depart(4)
print("remaining car"+str(n.park.items))
n.depart(1)
print("remaining car"+str(n.park.items))
n.depart(7)

