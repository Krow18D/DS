class Node:
    def __init__(self,data,left = None,rigth = None):
        self.data = data
        self.left = left
        self.rigth = rigth
    def __str__(self):
        return str(self.data)

def insert(wr,data):
    if wr == None:
        return Node(data)
    else:
        if data < wr.data:
            wr.left = insert(wr.left,data)
        else:
            wr.rigth = insert(wr.rigth,data)
    return wr

def _printSideway(wr,level):
    if wr != None:
        _printSideway(wr.rigth,level+1)
        print('   '*level,wr.data)
        _printSideway(wr.left,level+1)

def printSideway():
    _printSideway(root,0)

root = Node(5)
insert(root,6)
print(root.left,' ',root.rigth)
printSideway()

# class BST:
#     def __init__(self,root = None):
#         self.root = root
    
#     def addI(self,data):
#         if self.root == None:
#             self.root = Node(data)
#         else:
#             wr = self.root
#             while True:
#                 if data < wr.data:
#                     if wr.left == None:
#                         wr.left = Node(data)
#                         break
#                     wr = wr.left
#                 else:
#                     if wr.rigth == None:
#                         wr.rigth = Node(data)
#                         break
#                     wr = wr.rigth

#     def _add(self,data,wr):
#         if data < wr.data:
#             if wr.left==None:
#                 wr.left = Node(data)
#                 return
#             self._add(data,wr.left)
#         else :
#             if wr.rigth==None:
#                 wr.rigth = Node(data)
#                 return
#             self._add(data,wr.rigth)


#     def add(self,data):
#         if self.root == None:
#             self.root = Node(data) 
#         else:
#             self._add(data,self.root)

#     def _inorder(self, wr):
#         if wr == None:
#             return 
#         else:
            
#             self._inorder(wr.left)
#             print(wr.data)
#             self._inorder(wr.rigth)
            
#     def inorder(self):
#         self._inorder(self.root)
    
#     def _printSideway(self,wr,level):
#         if wr != None:
#             self._printSideway(wr.rigth,level+1)
#             print("   "*level,wr.data)
#             self._printSideway(wr.left,level+1)


#     def printSideway(self):
#         self._printSideway(self.root,0)


# def printK(n, reverse=0, save_n=0, print_row=False):
#     if save_n == 0:
#         save_n = n
#     if print_row == True:
#         if n == 0:
#             return
#         print('*',end='')
#         printK(n-1,save_n=save_n, print_row=True, reverse=reverse)
#     elif reverse == 0:
#         if n == 0:
#             printK(n+1,save_n=save_n, reverse=1)
#         else:
#             printK(n,save_n=save_n, print_row=True, reverse=reverse)
#             print()
#             printK(n-1,save_n=save_n, reverse=reverse)
#     else:
#         if n == save_n+1:
#             return
#         else:
#             printK(n,save_n=save_n, print_row=True, reverse=reverse)
#             print()
#             printK(n+1,save_n=save_n, reverse=reverse)


# # printK(5)
# def print_row(n):
#     if n == 0:
#         print()
#     else:
#         print('*',end='')
#         print_row(n-1)

# def run(n, increase):
#     if increase == False:
#         if n != 0:
#             print_row(n)
#             run(n-1, False)
#     else:
#         if n != 0:
#             run(n-1, True)
#             print_row(n)

# def printK_V2(n):
#     run(n, False)
#     run(n, True)

# printK_V2(5)
# print_row(5)


# n = Node(2)
# tree = BST(n)
# tree.add(5)
# tree.add(1)
# tree.add(6)
# tree.inorder()

# print(n.left," ",n.rigth.left)
# tree.printSideway()