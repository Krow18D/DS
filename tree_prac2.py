class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
def add(root,data):
    if root == None:
        return Node(data)
    else:
        if data < root.data:
            root.left = add(root.left,data)
        else:
            root.right = add(root.right,data)
    return root

def inorder(root):
    if root !=None:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)


def printSideway(root,level=0):
    if root != None:
        printSideway(root.right,level+1)
        print("   "*level,root.data,'-',high(root))
        printSideway(root.left,level+1)

def high(root):
    if root == None:
        return -1
    else:
        hl = high(root.left)
        hr = high(root.right)
        if hl >hr:
            return hl+1
        else:
            return hr+1

def highdata(root,data):
    if root.data == data:
        return high(root)
    else:
        if data < root.data:
            return highdata(root.left,data)
        else:
            return highdata(root.right,data)



def search(root,data):
    if root == None:
        return None
    elif root.data == data:
        return data
    else:
        if data < root.data:
            return search(root.left,data)
        else:
            return search(root.right,data)

def depth(root,data):
    if data == search(root,data):
        if root.data == data:
            return 0
        else:
            if data < root.data:
                return 1+depth(root.left,data)
            else:
                return 1+depth(root.right,data)

def path(root,data):
    if data == search(root,data):
        if root.data == data:
            print(data)
        else:
            print(root.data,end=' ')
            if data < root.data:
                return path(root.left,data)
            else:
                return path(root.right,data)

# def rank(root,data):
#     r=0
#     if root == None:
#         return 0
#     else:
#         if root.data<=data:
#             r+=1
#         return r+rank(root.left,data)+rank(root.right,data)
def rank2(root,i=1):
    if root.left != None:
        i=rank2(root.left,i)+1
    print('Rank of',root.data,'=',i)
    if root.right != None:
        i=rank2(root.right,i+1)
    return i
def delbai(root):
    if root == None:
        return None
    else:
        if root.left and not root.left.left and not root.left.right:
            root.left = None
        if root.right and not root.right.left and not root.right.right:
            root.right = None
        delbai(root.left)
        delbai(root.right)
def rightmost(root):
    if not root.right:
        return root
    else:
        return rightmost(root.right)
        
def delNode(root,data):
    if root == None:
        return root
    elif root.data == data:
        if  not root.right and not root.left:
            return None
        elif root.left and not root.right:
            return root.left
        elif root.right and not root.left:
            return root.right    
        else:
            pred = rightmost(root.left)
            root.data = pred.data
            root.left = delNode(root.left,pred.data)
        return root
    else:
        if data < root.data:
            root.left = delNode(root.left,data)
        else:
            root.right = delNode(root.right,data)
        return root
    


root = None
l=[14,15,6,1,2,13,0,16,17,-1]
for i in l:
    root = add(root,i)

# inorder(root)
# print()
printSideway(root)
# print(high(root))
# print(search(root,16))
#print(depth(root,14))
# path(root,13)
# delbai(root)
# printSideway(root,0)
# print(high(root))
# print()
# delNode(root,6)
# delNode(root,2)
# printSideway(root)
# print(rightmost(root))
rank2(root)
# print(highdata(root,16))
# delbai(root)
# printSideway(root)
