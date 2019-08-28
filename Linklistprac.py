class Node:
    def __init__(self,data,next = None):
        self.data = data
        if(next == None):
            self.next=None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
    def setData(self,x):
        self.data = x
    def setNext(self,x):
        self.next = x
class Linklist:
    def __init__(self,head = None):
        if(head == None):
            self.head = self.tail = None
            self.size = 0
        else :
            self.head = head
            self.size = 1
            t=self.head
            while(t.next!=None):
                self.size+=1
                t=t.next
            self.tail = t
    def __str__(self):
        s="Linklist = [ "
        t= self.head
        while(t!=None):
            s+=str(t.getData())+" "
            t=t.next
        return s+"]"
    def addNode(self,x):
        node = Node(x)
        if(self.size==0):
            self.head = self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node
        self.size+=1
    def addHead(self,x):
        node = Node(x)
        if(self.size==0):
            self.head = self.tail = node
        else :
            node.next = self.head
            self.head = node
        self.size+=1
    def isIn(self,x):
        if(self.size==0):
            return False
        else:
            t=self.head
            while(t!=None):
                if(t.getData()==x):
                    return True
                t=t.next
            return False
    def before(self,x):
        if(self.size == 0):
            return "List Empty"
        elif(x==self.head.getData()):
            return None
        elif(self.isIn(x)):
            t=self.head
            while(t!=None):
                if(t.next.getData()==x):
                    return t
                t=t.next
        else:
            return "None Data"
    def remove(self,x):
        if(self.isIn(x)and (self.size==0 or self.size==1)):
            self.head = self.tail = None
            self.size=0
        elif(self.isIn(x)):
            if(self.head.getData() == x):
                self.head = self.head.next
            elif(self.tail.getData() == x):
                self.tail = self.before(x)
                self.tail.setNext(None)
            else:
                t= self.head
                while(1):
                    if(t.getData()==x):
                        self.before(x).next = t.next
                        break
                    t=t.next
            self.size-=1
    def removeHead(self):
        if(self.size == 0 or self.size==1):
            self.size=0
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.size-=1
    def removeTail(self):
        if (self.size == 0 or self.size == 1):
            self.size = 0
            self.head = self.tail = None
        else:
            self.tail = self.before(self.tail.getData())
            self.tail.setNext(None)
            self.size-=1

n3=Node(3)
n2=Node(2,n3)
n1=Node(1,n2)
l = Linklist(n1)
l.addNode(4)
l.addHead(0)
print(l)
print(l.isIn(2))
print(l.before(4))
l.remove(0)
l.removeHead()
l.remove(2)
l.remove(3)
l.remove(4)
l.remove(2)
l.addNode(2)
l.addNode(3)
l.addHead(1)
l.addHead(4)
print(l," ",l.head," ",l.tail)
l.remove(2)
print(l)