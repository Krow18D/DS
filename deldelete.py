class Node:
    def __init__(self,data,next=None):
        self.data = data
        if(next == None):
            self.next = None
        else:
            self.next = next
    def getData(self):
        return str(self.data)
    def setData(self,x):
        self.data = x
    def setNext(self,x):
        self.next = x
    def __str__(self):
        return str(self.data)
class Linklist:
    def __init__(self,head = None):
        if(head == None):
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            self.size = 1
            t=self.head
            while(t.next!=None):
                self.size+=1
                t=t.next
            self.tail = t
    def __str__(self):
        out="LL = [ "
        t=self.head
        while(t!=None):
                out+=str(t.getData())+" "
                t=t.next
        return out+"]"
    def addNode(self,x):
        node=Node(str(x))
        if(self.size == 0):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size+=1
    def isIn(self,x):
        if(self.size == 0 ):
            False
        else:
            t=self.head
            while(t!=None):
                if(t.getData()==str(x)):
                    return True
                t=t.next
            return False        
        

def createList(list_):
    ll = Linklist()
    l = list_
    print("list_ = ",l)
    for i in l:
        ll.addNode(i)
    return ll

def delRepeat(linklist_):
        l_temp = Linklist()
        t=linklist_.head
        while(t!=None):
            if(not l_temp.isIn(t.getData())):
                l_temp.addNode(t)
            t=t.next
        print(t)
        linklist_.head = l_temp.head
        linklist_.tail = l_temp.tail
        linklist_.size = l_temp.size


l = [c for c in input("input: ").split()]
print("l = ",l)
h = createList(l)
delRepeat(h)
print(h)