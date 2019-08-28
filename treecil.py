
class node:
    def __init__(self,data,l=None,r=None):
        self.data = data
        self.left = l
        self.right = r
    def __str__(self):
        return str(self.data)

def add(r,data):
    if r == None :
        return node(data)
    else:
        if data < r.data :
            r.left = add(r.left,data)
        else:
            r.right = add(r.right,data)
        return r

def inOrder(r):
    if r != None :
        inOrder(r.left)
        print(r,end =' ')
        inOrder(r.right)

def preOrder(r):
    if r != None :
        print(r,end =' ')
        preOrder(r.left)
        preOrder(r.right)

def postOrder(r):
    if r != None :
        postOrder(r.left)
        postOrder(r.right)
        print(r,end =' ')

def printSideway(r,level=0):
    if r != None :
        printSideway(r.right,level+1)
        print('   '*level,r)
        printSideway(r.left,level+1)
        
################################################
def search(r,data):
    if r == None :
        return None
    elif data == r.data :
        return r 
    else:
        if data < r.data :
            return search(r.left,data)
        else:
            return search(r.right,data)
def pathReturnStr(r,data):
    if r == None :
        return '->HAVE NO THIS DATA'
    else:
        if r.data == data :
            return '->'+str(r)
        else:
            s = '->' + str(r)
            if data >= r.data :
                s += pathReturnStr(r.right,data)
            else:
                s += pathReturnStr(r.left,data)
            return s
def path(r,data):
    if r == None :
        print('->NO HAVE DATA')
    elif r.data == data :
        print('->',data,sep ='')
    else:
        print('->',r,sep ='',end ='')
        if data >= r.data :
            path(r.right ,data)
        else:
            path(r.left ,data)

def rightMost(r):
    if r.right == None :
        return r
    else:
        return rightMost(r.right)

def delete(r,data):
    if r == None :
        return r
    elif r.data == data :
        if r.left == None and r.right == None:
            return None
        elif r.left == None and r.right != None :
            return r.right
        elif r.left != None and r.right == None :
            return r.left
        else:
            predecessor = rightMost(r.left)
            print('predecessor = ',predecessor)
            r.data = predecessor.data
            r.left = delete(r.left,predecessor.data)
        return r   
    else:
        if r.data > data :
            r.left = delete(r.left,data)
        else:
            r.right = delete(r.right,data)
        return r
        
################################################

r = None 
l = [3,2,12,1,7,17,5,11,13,19,4,6,9,15,18,20,8,10,14,16]
for i in l :
    r = add(r,i)
inOrder(r)
print()
printSideway(r)

#print('search 15 ',search(r,15))
#print('search  7 ',search(r,7))

#print(pathReturnStr(r,14))
#print(pathReturnStr(r,18))
#print(pathReturnStr(r,7))
#print('path  no return')
#path(r,14)
#path(r,18)
#path(r,7)

print('-----------------')
#print('delete 18')
delete(r,12)
delete(r,11)
printSideway(r)
