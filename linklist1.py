class Node:
    def __init__(self,data,next = None):
        self.data = data
        if(next == None):
            self.next = None
        else :
            self.next = next
    def __str__(self):
        return str(self.data)
    def setData(self,x):
        self.data = x
    def setNext(self,x):
        self.next = x
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
class linklist:
    def __init__(self,head = None):
        if(head == None):
            self.size = 0
            self.head = self.tail = None
        else:
            self.size=1
            self.head = head
            t=self.head
            while(t.next!=None):
                self.size+=1
                t = t.next
            self.tail=t

    def __str__(self):
        t = self.head
        s = "Linklist = [ "
        while (t!= None):
            s+=str(t)+" "
            t = t.next
        return s+"]"

    def addNode(self,x):
        n = Node(x)
        if (self.size == 0):
            self.head = self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self.size+=1
    def addHead(self,x):
        n=Node(x)
        if(self.size==0):
            self.head = self.tail = n
        else:
            n.setNext(self.head)
            self.head=n
        self.size+=1

    def size(self):
        return self.size
    def isIn(self,x):
        t=self.head
        if(self.size>0):
            while (t != None):
                if (x==t.getData()):
                    return True
                t=t.next
            return False
        else:
            return False
    def before(self,x):
        if(self.size==0):
            return "List Empty"
        elif(self.head.getData() == x):
            return None
        elif(not self.isIn(x)):
            return "None data"
        else:
            t=self.head
            while(1):
                if(t.next.getData()==x):
                    return t
                t=t.next

    def remove(self,x):
        if(self.size==0):
            return "List Empty"
        elif(x==self.head.getData()):
            self.head=self.head.next
        elif(x==self.tail.getData()):
            self.tail = self.before(self.tail.getData())
            self.tail.setNext(None)
        elif(self.isIn(x)):
            t=self.head
            while(1):
                if(x==t.getData()):
                    print(self.before(x))
                    self.before(x).setNext(t.next)
                    break
                t=t.next
        self.size-=1

    def removeHead(self):
        if (self.size == 0):
            print("List Empty")
        else:
            if(self.size==1):
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.size-=1

    def removeTail(self):
        if (self.size == 0):
            print("List Empty")
        else:
            if(self.size==1):
                self.head = self.tail = None
            else:
                self.tail = self.before(self.tail.getData())
                self.tail.setNext(None)
            self.size-=1


n3=Node(3)
n2=Node(2,n3)
n1=Node(1,n2)
print(n1)
l=linklist(n1)

print(l)
l.addNode(4)
print(n3.getNext())
print(l)
print(l.isIn(1))
print(l.isIn(3))
print(l.isIn(4))
l.addNode(5)
print(l)
l.addHead(0)
print(l)
print(l.isIn(0))
print(l.before(3))
print(l.before(6))
print(l)
l.remove(4)
print(l)
l.removeHead()
print(l)
l.removeTail()
print(l)
print(l.tail)
l.removeTail()
print(l.tail)
print(l)
l.remove(2)
print(l.tail)
print(l)

