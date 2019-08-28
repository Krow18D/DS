class Node:
    def __init__(self,data,next=None):
        self.data = data
        if(next == None):
            self.next = None
        else:
            self.next = next

def creatList(list_):
    head= Node("dum")
    l=head
    for i in list_:
        l.next = Node(i)
        l = l.next
    return head
def printList(head):
    l = head.next
    out=""
    while l:
        out+=str(l.data)+" "
        l=l.next
    print(out)


l = [int(c) for c in input("input:").split()]
h = creatList(l)
printList(h)
revList(h.next)
printList(h)
