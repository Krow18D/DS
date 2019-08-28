class Node:
    def __init__(self,data,next=None):
        self.data = data 
        if(next == None):
            self.next = None
        else:
            self.next = next
class Linklist:
    def __init__(self,head=None):
        if(head == None):
            self.head = self.tail = None
            self.size =0
        else:
            self.head = head
            self.size=1
            t=self.head
            while(t):
                self.size+=1
                t=t.next
            self.tail = t
    def addNode(self,x):
        node = Node(x)
        if(self.size==0):
            self.head=self.tail =node
        else:
            self.tail.next = node
            self.tail = node
        self.size+=1
    def isIn(self,x):
        t=self.head
        while(t):
            if(t.data==str(x)):
                return True
            t=t.next
        return False
def createList(list_):
    l = Linklist()
    for i in list_:
        l.addNode(i)
    return l
def printList(l_list):
    out = ""
    t=l_list.head
    while t:
        out+=str(t.data)
        t=t.next
    print(out)
def delRepeat(l_list):
    l = Linklist()
    t=l_list.head
    while t:
        if(not l.isIn(t.data)):
            l.addNode(t.data)
        t=t.next
    l_list.head , l_list.tail = l.head , l.tail
    l_list.size = l.size


n3 = Node('3')
n2 = Node('2',n3)
n1 = Node('1',n2)
l1 = Linklist(n1)
print(l1.isIn(1))
print(l1.isIn(2))
print(l1.isIn(3))

l = [c for c in input("input: ").split()]
print("l = ",l)
h=createList(l)
printList(h)
delRepeat(h)
printList(h)